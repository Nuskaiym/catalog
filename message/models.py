from django.db import models


class Message(models.Model):
    user_name = models.CharField(help_text='Ваше имя', max_length=30)
    phone = models.IntegerField(help_text='Телефон')
    email = models.EmailField(help_text='Почта',)
    title = models.CharField(help_text='Тема',max_length=100)
    text = models.TextField(help_text='Текст сообщения',)

    def __str__(self):
        return self.title

