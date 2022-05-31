# Telegram TODO Bot by pyTelegramBotAPI
import telebot

from my_token import TOKEN

bot = telebot.TeleBot(TOKEN)

tasks = {}
tasks_complited = {}

HELP = '''
/help - Вывести текущую справку
/add - добавить задачу в список (дата, задача)
/show - показать задачу на дату
/show_all - показать все задачи
/delete - удалить задачу на дату
/done - отметить задачу на дату выполненной
'''

def add_todo(task_date, task):
    if task_date in tasks:
        tasks[task_date].append(task)
    else:
        tasks[task_date] = []
        tasks[task_date].append(task)
    print(f'Задача {task} на дату {task_date} добавлена')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Вас приветствует бот ! Нажмите /help для справки")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['add', 'todo'])
def add_task(message):
    in_text = message.text.split(' ', 2)
    date = in_text[1].lower()
    task = in_text[2]
    add_todo(date, task)
    text = f'Задача {task} добавлена на дату {date}'
    bot.reply_to(message, text)


@bot.message_handler(commands=['show', 'print'])
def show(message):
    in_text = message.text.split(' ', 1)
    date = in_text[1].lower()
    text = ''
    if date in tasks:
        text = f'{date.upper()}\n'
        for task in tasks[date]:
            text = f'{text} [ ] {task}\n'
    else:
        text = 'Задач на эту дату нет'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show_all'])
def show_all(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")


@bot.message_handler(commands=['delete'])
def delete(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")


@bot.message_handler(commands=['done'])
def done(message):
    bot.reply_to(message, "Вас приветствует бот ! Нажмите /help для справки")


if __name__ == '__main__':
    # bot.polling()
    bot.infinity_polling()  # бесконечный бот
