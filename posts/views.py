from django.contrib.auth.decorators import login_required

from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView,  DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from .froms import CommentForm, PostForm
from .models import Post, PostComment

from django.contrib.messages.views import SuccessMessageMixin


from .forms import PostForm



# CBV- Классовое представление
# FBV- Функциональное представление

# ListView - Представление для получения списка данных из модели
class PostListView(ListView):
    """
    дома написать
    """
    model = Post  # Модель объекта, который мы должны отобразить
    queryset = Post.objects.filter(status = "pb") # Можно задать кастомный queryset
    template_name = "post/index.html"  # путь к нашему шаблону
    context_object_name = "posts"
    paginate_by = 50
    ordering = ['-created_at']


# CreateView Представление  для добавления нового объекта в БД
class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    # fields = ["title", "description"] # Автоматически создает форму по указанным полям
    form_class = PostForm  # Можно использовать свою кастомную форму
    template_name = "posts/form.html"
    # context_object_name = "post"
    success_url = reverse_lazy("posts_list")  #
    success_message = "Пост был успешно создан "

# UpdateView - Представление для изменения существующего объекта
class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/form.html"
    success_url = reverse_lazy("posts_list")
    success_message = "Пост был успешно обновлен"
    pk_url_kwarge = "pk" # Имя параметра в URL для поиска по pk

# DetailView - Представление для отображения одного объекта
class PostDetailView(DetailView):
    model = Post
    # queryset =  Post.object.filter(status = "pb")
    context_object_name = "post"
    template_name = "posts/detail.html"



# DeleteView - Представление для удаления объекта
class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("posts_list")
    success_message = "Пост был успешно удален"


def get_post_user(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    user = request.user


# Лайки
@login_required
@require_POST # Можно только делать POST-запрос
def like_post(request: HttpRequest, post_id: int):
    post, user = get_post_user(request, post_id)
    if post.likes.filter(user=user).exist():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        if post.dislikes.filter(user=user).exists():
            post.dislikes.remove(user)
        liked = True
    return JsonResponse(
        {
            "liked": liked,
            "total_likes": post.likes.count()
        }
    )

# Дизлайки
@login_required
@require_POST # Можно только делать POST-запрос
def dislike_post(request: HttpRequest, post_id: int):
    post, user = get_post_user(request, post_id)
    if post.dislikes.filter(user=user).exist():
        post.dislikes.remove(user)
        disliked = False
    else:
        post.dislikes.add(user)
        if post.likes.filter(user=user).exists():
            post.likes.remove(user)
        disliked = True
    return JsonResponse(
        {
            "disliked": disliked,
            "total_dislikes": post.dislikes.count()
        }
    )


# Написать, Изменить, Удалить комментарии


@login_required
@require_POST # Можно только делать POST-запрос
def add_comment(request: HttpRequest, post_id: int):
    post, user = get_post_user(request, post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = user
        comment.save()
    return redirect("post_detail", pk=post_id)



@login_required
@require_POST # Можно только делать POST-запрос
def change_comment(request: HttpRequest, comment_id: int):
    comment = get_object_or_404(PostComment, id=comment_id)
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid() and comment.user == request.user:
        form.save()
    return redirect("post_detail", pk=comment.post.pk)

@login_required
@require_POST # Можно только делать POST-запрос
def delete_comment(request: HttpRequest, comment_id: int):
    comment = get_object_or_404(PostComment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect("post_detail", pk=comment.post.pk)

