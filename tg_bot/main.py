import telebot
from project.config import token
import django
django.setup()
from project.models import Request
import time

token = token
bot = telebot.TeleBot(token)
users = []



# @bot.message_handler(commands=['start'])
# def user_save(message):
#     user = message.chat.id
#     print(user)
#     if user not in users:
#         users.append(user)
#     msg = bot.send_message(message.from_user.id, 'Введите номер телефона: ')
#     bot.register_next_step_handler(send_message)
#     print(users)


# def send_message():
#     print(1)
#     request = Request.objects.last()
#     text=f'Добавлена заявка номер {request.id} из региона {request.region}'
#     for user in users:
#         print('hello')
#         bot.send_message(chat_id=user, text=text)
#     print(users)  
    
# def send_message(message):
#     
#     print(message.from_user.id)
#     bot.send_message(message.from_user.id, text='Hello')
#     # chat_id=523162388,
if __name__ == '__main__':
    bot.polling(none_stop=True)



