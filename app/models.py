"""
Наши моделки (ТАблицы В БД)
"""
from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    """
    Абстрактный класс миксин для добавления полей с временными шкалами

    Attributes:
    created_at (model.DateField) : Дата создания поста
    updated_at (model.DateField) : Дата обновления поста
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True # Чтобы сделать наш класс абстактным
# Create your models here.




