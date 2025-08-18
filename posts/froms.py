from django import forms
from posts.models import Post, PostComment


class PostForm(forms.ModelForm):
    pass


class CommentForm(forms.ModelForm):
    pass