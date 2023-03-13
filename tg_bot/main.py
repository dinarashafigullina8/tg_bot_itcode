import telebot
from project.config import token
from project.models import Request

token = token
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])  
def send_message():
    request = Request.objects.last()
    bot.send_message(chat_id=523162388, text=f'Добавлена заявка номер {request.id} из региона {request.region}')
    
if __name__ == '__main__':
    bot.polling(none_stop=True)


