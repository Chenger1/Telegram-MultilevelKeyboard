from typing import Optional

import keyboards


menu_storage = {
    'LEVEL_1': keyboards.level_1,
    'LEVEL_1:LEVEL_2': {
        'LEVEL_2_LIST': keyboards.level_2_list,
        'LEVEL_2_LIST:LEVEL_3_LIST': {
            'LEVEL_3_FILTER': keyboards.level_3_filter,
            'LEVEL_3_MY_LIST': keyboards.level_3_my_list
        },
        'LEVEL_2_DETAIL': keyboards.level_2_detail,
        'LEVEL_2_DETAIL:LEVEL_3_DETAIL': {
            'LEVEL_3_DETAIL': keyboards.level_3_detail
        }
    }
}


async def dispatcher(level: str) -> tuple[keyboards.ReplyKeyboardMarkup, str]:
    """ Returns right keyboard for each level
        You can modify it in different purposes.
        For example if you want to have several user groups
        You can get user_id as parameter and checks his group, etc.
    """
    keyboard_cor, prev_level = await find_in_dict(level, menu_storage)
    return keyboard_cor, prev_level


async def find_in_dict(level: str, storage: dict, prev_level: str = 'LEVEL_1') \
        -> Optional[tuple[keyboards.ReplyKeyboardMarkup, str]]:
    """
    RECURSIVE function
    Iterates over storage. If key == level - return level`s keyboard
    If not and value is dict - pass it to recursion function. Dictionary is a sublevel.
    So, we run recursive coroutine and pass - level, THIS KEY`S VALUE - that is i mean sublevel
    And current prev_level.
    If this coroutine returns result - return it on top. Otherwise continue iteration
    :param level: Level we want to reach
    :param storage: menu_storage
    :param prev_level: name of previous menu level
    """

    for key, value in storage.items():
        if key == level:
            return value, prev_level.split(':')[0]
        if isinstance(value, dict):
            result = await find_in_dict(level, value, key)
            if result:
                return result
