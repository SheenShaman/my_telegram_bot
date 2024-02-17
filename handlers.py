import webbrowser
from config import bot


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://pypi.org/project/pyTelegramBotAPI/')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help information</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')
