from django.db import models
from django.urls import reverse

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
        "df": "Draft",
        "pb": "Published"
    }
    title = models.CharField(max_length=255, verbose_name="Название поста")
    slug = models.SlugField(null=True, blank=True, verbose_name="Слаг")
    description = models.TextField(blank=True, default="", verbose_name="Описание поста")
    status = models.CharField(max_length=2, choices=STATUS, verbose_name="Статус публикации")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Дата публикации")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Пользователь поста")
    tags = models.ManyToManyField(Tag, verbose_name="Тег")
    likes = models.ManyToManyField(User, related_name="likes")
    dislikes = models.ManyToManyField(User, related_name="dislikes")

    def __str__(self):
        return f"{self.title} - {self.user} - {self.published_at}"

    def get_likes_count(self):
        return self.likes.count()

    def get_dislikes_count(self):
        return self.dislikes.count()

    def get_first_image(self):
        if self.images.all():
            return self.images.all()[0].image.url
        return None


    # Он генерирует ссылку для просмотра нашего обьекта (обычно detail-страницу)
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})



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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments" ,verbose_name="Комментируемый пост")
