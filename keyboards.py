from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


level_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Some list'),
    KeyboardButton('Some details')
).add(
    KeyboardButton('Back')
)


level_2_list = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Filter list'),
    KeyboardButton('Open my list')
).add(
    KeyboardButton('Back')
)


level_2_detail = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Open more details')
).add(
    KeyboardButton('Back')
)

level_3_my_list = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('My list can be here'),
).add(
    KeyboardButton('Back')
)


level_3_filter = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('You can return now'),
).add(
    KeyboardButton('Back')
)


level_3_detail = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Details can be here')
).add(
    KeyboardButton('Back')
)
