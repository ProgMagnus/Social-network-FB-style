# Generated by Django 3.2.5 on 2021-09-24 16:30

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=200, verbose_name='Фамилия')),
                ('bio', models.TextField(default='Пустая биография', max_length=300, verbose_name='О себе')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='Э-мейл')),
                ('country', models.CharField(blank=True, max_length=200, verbose_name='Страна')),
                ('avatar', models.ImageField(default='avatar.png', upload_to='profile_images/%Y/%m/%d/', verbose_name='Изображение профиля')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания профиля')),
                ('friends', models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL, verbose_name='Друзья')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
