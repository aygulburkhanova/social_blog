from django.db import models

from app.models import TimeStampMixin
from django.urls import reverse

class Tag(TimeStampMixin):
    """"
    Теги наших постов


    Attributes:
       title  (model.CharField):  Название тега
       slug (models.SlugField): Стог тега хештеги
       created_at (model.DateField) : Дата создания тега
       updated_at (model.DateField) : Дата обновления тега
    """

    title = models.CharField(max_length=255, verbose_name="Название тега")
    slug = models.SlugField(null=True, blank=True, verbose_name="Стог тега")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.pk})
