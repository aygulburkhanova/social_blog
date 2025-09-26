from django import forms
from django.contrib.auth.forms import (
    UserCreationForm as BaseUserCreationForm,
    UserChangeForm as BaseUserChangeForm
)
from django.contrib.auth.models import User

from .models import Profile
class UserCreationForm(BaseUserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        # Моделька к которому присоединена Форма
        model = User
        # Поля которые должны отобразиться
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # Виджеты
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        }
        # Лейблы
        labels = {
            "username": "Username",
            "email": "Email",
            "first_name": "First name",
            "last_name": "Last name",
            "password1": "Password",
            "password2": "Confirm password",
        }
        # Help Texts
        help_texts = {
            "username": "Write your username here",
            "email": "Write your email address here",
            "first_name": "Write your first name here",
            "last_name": "Write your last name here",
            "password1": "Write your password here",
            "password2": "Write your password here",
        }


class UserChangeForm(BaseUserChangeForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        # Виджеты
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
        }
        # Лейблы
        labels = {
            "username": "Username",
            "email": "Email",
            "first_name": "First name",
            "last_name": "Last name",
        }
        # Help Texts
        help_texts = {
            "username": "Write your username here",
            "email": "Write your email address here",
            "first_name": "Write your first name here",
            "last_name": "Write your last name here",
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "bio")