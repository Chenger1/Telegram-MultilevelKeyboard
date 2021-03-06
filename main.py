from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text

from config import Token

from dispatcher import dispatcher


storage = MemoryStorage()  # User RedisStorage in production
#  Because MemoryStorage flush all data after reboot and ['prev_level'] keys will be deleted
# So user wont be able to manage keyboard
bot = Bot(token=Token, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(Text(equals=['Back']))
async def back(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        keyboard, prev_level = await dispatcher(data.get('prev_level', 'LEVEL_1'))
        message_text = 'Back to previous level'
        await message.answer(message_text, reply_markup=keyboard)
        data['prev_level'] = prev_level  # ALWAYS save new prev_level to state


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message, state: FSMContext):
    keyboard, prev_level = await dispatcher('LEVEL_1')
    await message.answer('Hello', reply_markup=keyboard)
    await state.update_data(prev_level=prev_level)


@dp.message_handler(Text(equals=['Some list']))
async def some_list(message: types.Message, state: FSMContext):
    keyboard, prev_level = await dispatcher('LEVEL_2_LIST')
    await message.answer('Menu - level 2 lists', reply_markup=keyboard)
    await state.update_data(prev_level=prev_level)


@dp.message_handler(Text(equals=['Some details']))
async def some_list_2(message: types.Message, state: FSMContext):
    keyboard, prev_level = await dispatcher('LEVEL_2_DETAIL')
    await message.answer('Menu - level 2 details', reply_markup=keyboard)
    await state.update_data(prev_level=prev_level)


@dp.message_handler(Text(equals=['Filter list']))
async def some_list_3(message: types.Message, state: FSMContext):
    keyboard, prev_level = await dispatcher('LEVEL_3_FILTER')
    await message.answer('Menu - level 3 - filtered', reply_markup=keyboard)
    await state.update_data(prev_level=prev_level)


@dp.message_handler(Text(equals=['Open more details']))
async def some_list_4(message: types.Message, state: FSMContext):
    keyboard, prev_level = await dispatcher('LEVEL_3_DETAIL')
    await message.answer('Menu - level 3 - more details', reply_markup=keyboard)
    await state.update_data(prev_level=prev_level)


@dp.message_handler(Text(equals=['Open my list']))
async def some_list_5(message: types.Message, state: FSMContext):
    keyboard, prev_level = await dispatcher('LEVEL_3_MY_LIST')
    await message.answer('Menu - level 3 - my list', reply_markup=keyboard)
    await state.update_data(prev_level=prev_level)


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_shutdown=on_shutdown)
