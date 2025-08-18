from audioop import reverse

from django.db import models
from app.models import TimeStampMixin
from posts.models import User, Post
from django.urls import reverse

class Collection(TimeStampMixin):
    """"
    Колекция избранных


    Attributes:
        name(models.Charfield): Название колекции
        is_private(models.BoleanFireld): Приватность
        created_at (model.DateField) : Дата создания Колекции
        updated_at (model.DateField) : Дата обновления Колекции

        user(User): Пользователь создавший колекцию
    """
    name = models.CharField(max_length=100, blank=False, verbose_name=" Название коллекции")
    is_private = models.BooleanField(default=True, verbose_name="Приватная коллекция")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец коллекции")

    def __str__(self):
        return f"{self.name} - {self.user.username}"
    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"pk": self.pk})


class CollectionItems(TimeStampMixin):
    """
    Избранные

    Attributes:
        created_at (model.DateField) : Дата создания избранного
        updated_at (model.DateField) : Дата обновления избранного
        collections (Collection): Колекуия к которому она пренадлежит

        user(User): Пользователь создавший колекцию
        post(Post): Пост

    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Добавивший пользователь")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Добавленный пост")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="Коллекция")


