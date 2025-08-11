from django.contrib import admin

# Register your models here.
from tags.models import Tag


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ["title", "view_post_count"]

    list_filter = ["created_at"]
    search_fields = ["title"]

    list_per_page = 10

    @admin.display(description="Количество постов")
    def view_post_count(self, obj:Tag):
        return  0