from django.contrib import admin

from posts.models import Post, PostImage


class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 0
    min_num = 0
    max_num = 3


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    # Помогает в Списке Показывать какие нужны для показа
    list_display = [
        "title", "status", "user", "published_at", "view_like_count", "view_dislike_count", "view_comment_count"
    ]
    # Убирает с Формы в Админке Поле которое не нужно
    exclude = ["published_at", "likes", "dislikes"]
    # Какие поля можно изменять в Списки
    list_editable = ["status"]
    # По каким Полям должна быть фильтрация
    list_filter = ["created_at"]
    # Поиск
    search_fields = ["title"]
    # Пагинация
    list_per_page = 20
    # Инлайн Модельки
    inlines = [PostImageInline]

    @admin.display(description="Лайки")
    def view_like_count(self, obj: Post):
        return 0

    @admin.display(description="ДизЛайки")
    def view_dislike_count(self, obj: Post):
        return 0

    @admin.display(description="Комменты")
    def view_comment_count(self, obj: Post):
        return 0
