"""
Наш основной машрутизатор
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #Путь до Админ панель
    path('', include("app.urls"))
]


