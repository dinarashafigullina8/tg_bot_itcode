import telebot
from config import token


token = token
bot = telebot.TeleBot(token)
applications = []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте')

@bot.message_handler(commands=['new_app'])
def new_application(message):
    result = message.json['text'].split(' ')
    if len(result) != 3:
       bot.send_message(message.chat.id, text='Неверный формат заявки. Пример: /new_app Регион, номер заявки') 
    else:
        application = {'Регион': result[1][:-1], 'Номер заявки': result[2]}
        applications.append(application)
        print(applications)
        bot.send_message(message.chat.id, text='Успешно сохранено')
bot.polling(none_stop=True)    


