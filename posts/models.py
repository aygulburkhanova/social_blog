from django.db import models

from app.models import TimeStampMixin
from django.contrib.auth.models import User

from tags.models import Tag


class Post(TimeStampMixin):
    """
    Модель Постов наследуется от базового класса TimeStampMixin


    Attributes:
       title  (model.CharField):  Название поста
       slug (models.SlygField): Слог нашего поста
       description (models.CharField): Описание нашего поста
       status (models.CharField): Статус нашего поста
       created_at (model.DateField) : Дата создания поста
       updated_at (model.DateField) : Дата обновления поста
       published_at (model.DateField) : Дата публикации поста
       user (User) : пользователь создавший пост
    """
    STATUS = {
        "df": "Dtaft",
        "pb": "Published"
    }
    title = models.CharField(max_length=255, verbose_name="Название патса")
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS)
    published_at = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, through="Like", related_name="post_likes")



class PostImage(models.Model):
    """
    Хранит Изображение постов

     Attributes:
     image (ImageField): Изображение поста
     post (Post):  Пост к которому принадлежит изображение
    """
    image = models.ImageField(upload_to="post/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")



class PostComment(TimeStampMixin):
    """"
    Коментария нашего поста

    Attributes:
        body (models.Charfield): Техт коментария

        created_at (model.DateField) : Дата создания поста
        updated_at (model.DateField) : Дата обновления поста

        дома продолжит
    """


class Like(TimeStampMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")





