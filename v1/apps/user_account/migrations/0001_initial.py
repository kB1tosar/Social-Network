# Generated by Django 2.2.5 on 2019-09-23 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('second_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('skype', models.CharField(max_length=20, verbose_name='Skype')),
                ('country', models.CharField(max_length=20, verbose_name='Страна')),
                ('city', models.CharField(max_length=20, verbose_name='Город')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Никнейм')),
            ],
        ),
    ]
