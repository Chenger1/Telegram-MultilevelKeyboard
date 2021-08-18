# Telegram-MultilevelKeyboard
Example of creating multilevel keyboard with default buttons(ReplyMarkup) - not inline

The main idea is to put menu levels to dictionary, iterate over it to find particular level - and return matched keyboard.
If you want to test it:

1. Clone from repository
2. Create file config.py and put your bot token to variable 'Token'. Or just but token to bot


Keyboard can be either regular ReplyKeyboardMarkup or function(coroutine). For example, if we want to have different keyboard for different user groups. We can pass user_id or status to
dispatcher and make all necessary checks. 

Look at this project for more advanced example of using this idea: https://github.com/Chenger1/SwipeTelegramBot/blob/main/keyboards/default/dispatcher.py

Repository opens for proposals.
I know that algorithm  can be improved, so welcome
