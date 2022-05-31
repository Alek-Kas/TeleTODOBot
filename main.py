# Telegram TODO Bot
import telebot

from my_token import TOKEN

bot = telebot.TeleBot(TOKEN)

tasks = {}

HELP = ''' '''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")

@bot.message_handler(commands=['show'])
def send_welcome(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")

@bot.message_handler(commands=['add'])
def send_welcome(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")

@bot.message_handler(commands=['remove'])
def send_welcome(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")

if __name__ == '__main__':
    bot.polling()
    # bot.infinity_polling()  # бесконечный бот
