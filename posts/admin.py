from django.contrib import admin
from posts.models import Post, PostImage



class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 3
    min_num = 0
    max_num = 3

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Помогает в Списке какие поля для показа
    list_display = ["title", "status", "published_at", "user", "view_like_count", "view_dislike_count", "view_comment_count"]
    exclude = ["published_at"]  # Убирает с формы в админке поля которое не нужно


    # какие поля можно изменять в списке
    list_editable = ["status"]


    # По каким полям должна быть фильтрация
    list_filter = ["created_at"]

    # Поиск
    search_fields = ["title"]

    # Пагинация
    list_per_page = 20
    # Инлайн моделки
    inlines = [PostImageInline]





    # если не добавит obj выйдет ошибка

    @admin.display(description="Лайки")
    def view_like_count(self, obj: Post):
        return 0

    @admin.display(description="Дизлайки")
    def view_dislike_count(self, obj: Post):
        return 0

    @admin.display(description="Клмменты")
    def view_comment_count(self, obj: Post):
        return 0



