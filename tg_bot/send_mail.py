import smtplib
from project.config import password_sender
from project.models import Request


def send_email():
    sender = "dineirashafigulllina@gmail.com"
    password = password_sender
    request = Request.objects.last()
    message = f'Поступила заявка номер {request.id} из региона {request.region}'
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls
    
    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)
        print('Письмо успешно отправлено!')
        return 'Письмо успешно отправлено!'
        
    except Exception as _ex:
        return f"{_ex}\n Проверьте логин и пароль для почты"
    


    


