"""
Наши моделки (ТАблицы В БД)
"""

from django.db import models


class TimeStampMixin(models.Model):
    """
    Абстрактный класс миксин для добавления временных меток.

    Attributes:
        created_at (model.DateTimeField): Дата создания
        updated_at (model.DateTimeField): Дата обновления
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True # Чтобы сделать наш класс абстактным




