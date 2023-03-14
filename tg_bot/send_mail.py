import smtplib
from project.config import password_sender
import django
django.setup()
from project.models import Request
from email.mime.text import MIMEText


def send_email(message):
    sender = "dineirashafigulllina@gmail.com"
    password = password_sender


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        server.sendmail(sender, sender, msg.as_string())
        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    request = Request.objects.last()
    message = f'Поступила заявка номер {request.id} из региона {request.region}'
    print(send_email(message=message))

if __name__ == "__main__":
    main()
    


