from django import forms

from posts.models import Post, PostComment, PostImage


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'status', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={"placeholder": "Введите заголовок..."}),
            'description': forms.Textarea(attrs={"rows": "6", "placeholder": "Напишите что-то интересное..."}),
            'status': forms.Select(attrs={'class': 'form-control'}, choices=Post.STATUS),
            'tags': forms.SelectMultiple(),
        }


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        max_length=1024,
        widget=forms.Textarea(attrs={"placeholder": "Напишите комментарий..."}),
        help_text="Write your comment here.",
        label="Comment Body"
    )

    class Meta:
        model = PostComment
        fields = ('body',)


PostImageFormSet = forms.modelformset_factory(PostImage, form=PostImageForm, extra=3, can_delete=True)
