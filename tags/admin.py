from django.contrib import admin

from tags.models import Tag

@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    pass
