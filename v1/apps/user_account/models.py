from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='Никнейм',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(verbose_name='Фамилия', max_length=20)
    second_name = models.CharField(verbose_name='Имя', max_length=20)
    patronymic = models.CharField(verbose_name='Отчество', max_length=20)
    skype = models.CharField(verbose_name='Skype', max_length=20)
    country = models.CharField(verbose_name='Страна', max_length=20)
    city = models.CharField(verbose_name='Город', max_length=20)
