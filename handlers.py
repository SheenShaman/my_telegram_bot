import webbrowser

from config import bot
from telebot import types


@bot.message_handler(commands=['site', 'website'])
def site(message):
    """ Открывает сайт в браузере """
    webbrowser.open('https://pypi.org/project/pyTelegramBotAPI/')


@bot.message_handler(commands=['start'])
def main(message):
    """ Выводит приветствие """
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!')


@bot.message_handler(commands=['help'])
def main(message):
    """ Выводит Help information """
    bot.send_message(message.chat.id, '<b>Help information</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    """ Выводит приветствие при получении 'привет' или выводит id пользователя при 'id' """
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    """ Выводит 'Nice Photo!' при получении файла формата фото"""
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton("Перейти на сайт", url=))
    bot.reply_to(message, 'Nice Photo!')
