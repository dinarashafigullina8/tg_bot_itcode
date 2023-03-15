import telebot
from project.config import token
import django
django.setup()
from project.models import Request, User

token = token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def user_save(message):
    user_id = message.chat.id
    bot.send_message(message.chat.id, text='Здравствуйте')
    user = User.objects.get_or_create(user_id=user_id)

@bot.message_handler(commands=['stop'])
def user_delete(message):
    user_id = message.chat.id
    bot.send_message(message.chat.id, text='Всего доброго')
    User.objects.filter(user_id=user_id).delete()

users = list(User.objects.all().values_list('user_id',flat=True).order_by('user_id'))
print(users)
for user in  users:
    request = Request.objects.last()
    text=f'Поступила заявка номер {request.id} из региона {request.region}'
    print('ok')
    bot.send_message(chat_id=user, text=text) 

if __name__ == '__main__':
    bot.polling(none_stop=True)



