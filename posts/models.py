from django.db import models
from app.models import TimeStampMixin
from django.contrib.auth.models import User
from tags.models import Tag


class Post(TimeStampMixin):
    """
    Модель Постов наследуется от базового класса TimeStampMixin

    Attributes:
       title (model.CharField): Название поста
       slug (models.SlugField): Слаг нашего поста
       description (models.TextField): Описание нашего поста
       status (models.CharField): Статус нашего поста
       created_at (model.DateTimeField): Дата создания поста
       updated_at (model.DateTimeField): Дата обновления поста
       published_at (model.DateTimeField): Дата публикации поста

       user (User): пользователь создавший пост
       tags (ManyToManyField): Теги поста
       likes (ManyToManyField): Лайки поста
       dislikes (ManyToManyField): Дизлайки поста
    """
    STATUS = {
        "df": "Dtaft",
        "pb": "Published"
    }
    title = models.CharField(max_length=255, verbose_name="Название поста")
    slug = models.SlugField(null=True, blank=True, verbose_name="Слаг")
    description = models.TextField(blank=True, default="", verbose_name="Описание поста")
    status = models.CharField(max_length=2, choices=STATUS, verbose_name="Статус публикации")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь поста")
    tags = models.ManyToManyField(Tag, verbose_name="Тег")
    likes = models.ManyToManyField(User, through="Like", related_name="post_likes")
    dislikes = models.ManyToManyField(User, through="DisLike", related_name="post_dislikes")


    def __str__(self):
        return f"{self.title} - {self.user} - {self.published_at}"

    def get_likes(self):
        pass

    def get_dislikes(self):
        pass


    def get_absolute_url(self):
        pass



class PostImage(models.Model):
    """
    Хранит Изображение постов

      Attributes:
        image (ImageField): Изображение поста
        post (Post): Пост к которому принадлежит изображение
    """
    image = models.ImageField(upload_to="post/", verbose_name="Изображение")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images", verbose_name="Пост")



class PostComment(TimeStampMixin):
    """"
    Коментария нашего поста

     Attributes:
        body (models.TextField): Текст комментария
        created_at (model.DateTimeField): Дата создания комментария
        updated_at (model.DateTimeField): Дата обновления комментария
        user (User): Пользователь написавший комментарий
        post (Post): Пост

    """
    body = models.TextField(blank=False, verbose_name="Текст комментария")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Комментируемый пост")


class Like(TimeStampMixin):
    """
    Лайки постов

    Attributes:
        created_at (model.DateTimeField): Дата создания лайка

        user (User): пользователь поставивший лайк
        post (Post): Пост
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        unique_together = ("post", "user")


class DisLike(TimeStampMixin):
    """
    DisLike постов

    Attributes:
         created_at (model.DateField) : Дата создания лайка

         user (User) : пользователь создавший пост
         post(Post): Пост
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        unique_together = ("post", "user")

