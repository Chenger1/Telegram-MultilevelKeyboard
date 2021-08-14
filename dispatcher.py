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
    """ Return right keyboard for each level
        You can modify it in different pusposes.
        For example if you want to have several user groups
        You can get user_id as parameter and checks his group, etc.
    """
    keyboard_cor, path = await find_in_dict(level, menu_storage)
    return keyboard_cor, path


async def find_in_dict(level: str, storage: dict, path: str = '') -> tuple[keyboards.ReplyKeyboardMarkup, str]:
    """
    RECURSIVE function
    Iterates over storage. If key == level - return this callable (coroutine)
    If not and value is dict - pass it to recursion function. Dictionary is a sublevel.
    So, we run recursive coroutine and pass - level, THIS KEY`S VALUE - that is i mean sublevel
    And current path.
    If this coroutine returns result - return it on top. Other wire continue iteration
    :param level: Level we want to reach
    :param storage: menu_storage
    :param path: path for current level from top of the menu_storage. Uses in back_button
    """

    for key, value in storage.items():  # Maybe we can use iteration instead of recursion, for example with 'while'
        if key == level:
            path += f'/{key}'
            return value, path
        if isinstance(value, dict):
            path += f'/{key}'
            result = await find_in_dict(level, value, path)
            if result:
                return result
            path = '/'.join(path.split('/')[:-1])
            #  if we didn`t find the result - remove this path and iterate again


async def back_button(path: str) -> tuple[keyboards.ReplyKeyboardMarkup, str]:
    """
      Path looks like 'LEVEL_1:LEVEL_2/LEVEL_2_POSTS'. Split string to get previous level.
      Previous level ALWAYS has format 'LEVEL_1:LEVEL_2'. Split it to get 'LEVEL_1' - this level we want to rich to
      got back
      Pass this level to dispatcher
      :param path: path to current level
      :return: ReplyKeyboardMarkup
      """
    levels = path.split('/')
    last_level = levels[-2].split(':')[0]
    return await dispatcher(last_level)
