from django.db import models

class Request(models.Model):
    region = models.CharField(max_length=255, verbose_name='Заявки')
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
    
class User(models.Model):
    user_id = models.CharField(max_length=255)
