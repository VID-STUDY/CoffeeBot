from application import telegram_bot
from application.core import userservice
from application.resources import strings
from application.utils import bot as botutlis
from telebot.types import Message


def check_profile(message: Message):
    if not message.text:
        return False
    user_id = message.from_user.id
    user = userservice.get_user_by_telegram_id(user_id)
    if not user:
        return False
    language = user.language
    return strings.get_string('main_menu.profile', language) in message.text and message.chat.type == 'private'


def checker(message: Message):
    if not message.text:
        return False
    return botutlis.check_auth(message) and check_profile(message)


@telegram_bot.message_handler(commands=['profile'])
@telegram_bot.message_handler(content_types=['text'], func=checker)
def profile_handler(message: Message):
    global free_coffee
    chat_id = message.chat.id
    user_id = message.from_user.id
    language = userservice.get_user_language(user_id)
    current_user = userservice.get_user_by_id(user_id)
    if (current_user.count_orders % 10) == 9:
        free_coffee = '<b>Вы можете забрать следующий заказ бесплатно!</b>'
        telegram_bot.send_message(chat_id, text=(strings.get_string('all_coffee', language).format(current_user.count_orders, free_coffee)), parse_mode='HTML')
    else:
        free_coffee = ''
        telegram_bot.send_message(chat_id, text=(strings.get_string('all_coffee', language).format(current_user.count_orders, free_coffee)), parse_mode='HTML')
    botutlis.to_main_menu(chat_id, language)
