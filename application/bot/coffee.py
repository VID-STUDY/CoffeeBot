from application import telegram_bot as bot
from application.core import userservice
from application.resources import strings
from application.utils import bot as botutlis
from telebot.types import Message
from application.bot.orders import order_processor


def check_coffee(message: Message):
    if not message.text:
        return False
    user_id = message.from_user.id
    user = userservice.get_user_by_telegram_id(user_id)
    if not user:
        return False
    language = user.language
    return strings.get_string('main_menu.coffee', language) in message.text and message.chat.type == 'private'


def checker(message: Message):
    if not message.text:
        return False
    return botutlis.check_auth(message) and check_coffee(message)


@bot.message_handler(commands=['profile'])
@bot.message_handler(content_types=['text'], func=checker)
def coffee_handler(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    order_processor(message)
