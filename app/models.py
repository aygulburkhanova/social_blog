"""
Наши Модельки (Таблицы в БД)
"""
from django.contrib.auth.models import User
from django.db import models


class TimeStampMixin(models.Model):
    """
    Абстрактный Класс Миксин для добавление полей с времени шкалами

    Attributes:
        created_at (models.DateTimeField): Дата Создания Поста
        updated_at (models.DateTimeField): Дата Обновление Поста
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Чтобы сделать наш класс абстрактным



