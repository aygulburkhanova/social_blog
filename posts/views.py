from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from collections_app.forms import AddToCollectionForm
from posts.forms import CommentForm, PostForm, PostImageFormSet
from posts.models import Post, PostComment, PostImage
from posts.filters import PostFilter
from collections_app.models import Collection
# CBV - классовое представления
# FBV - функцианальное представление

# ListView - Представление для получение Списка данных из Модели
class PostListView(ListView):
    """

    """
    model = Post  # Модель обьекта которой нужно отобразить
    queryset = Post.objects.filter(status="pb")  # Можно задать кастомный QuerySet
    template_name = "posts/index.html"  # Путь к нашему шаблону HTML
    context_object_name = "posts"  # Имя переменной в шаблоне
    paginate_by = 50  # Пагинация
    ordering = ['-created_at']  # Сортировка
    filterset_class = PostFilter

    def get_queryset(self):  
        queryset = Post.objects.filter(status="pb").prefetch_related("tags")
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):  
        context = super(PostListView, self).get_context_data(**kwargs)
        context['filter'] = self.filterset
        context["collection_form"] = AddToCollectionForm(
            user=self.request.user) if self.request.user.is_authenticated else None
        context["collections"] = Collection.objects.filter(
            user=self.request.user) if self.request.user.is_authenticated else None
        return context


        





# CreateView - Представление для добавление нового обьекта в БД
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    # fields = ["title", "description"] # автоматически создает форму по указанным полям
    form_class = PostForm  # Можно использовать свою кастомную форму
    template_name = "posts/form.html"
    # context_object_name = "post" # form
    success_url = reverse_lazy("post_list")
    success_message = "Пост был успешно создан"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["images"] = PostImageFormSet(self.request.POST, self.request.FILES, queryset=PostImage.objects.none())
        else:
            data["images"] = PostImageFormSet(queryset=PostImage.objects.none())
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context["images"]
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        if images.is_valid():
            for f in images.cleaned_data:
                if f and "image" in f:
                    PostImage.objects.create(post=self.object, image=f["image"])
        return super().form_valid(form)


# UpdateView - Представление для изменение существующего обьекта в БД
class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    # fields = []
    form_class = PostForm
    template_name = "posts/form.html"
    success_url = reverse_lazy("post_list")
    success_message = "Пост был успешно обновлен"

    # pk_url_kwarg = "pk" # Имя параметра в URL для по pk
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["images"] = PostImageFormSet(self.request.POST, self.request.FILES, queryset=PostImage.objects.all())
        else:
            data["images"] = PostImageFormSet(queryset=PostImage.objects.all())
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context["images"]
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        if images.is_valid():
            for img_form in images:
                if img_form.cleaned_data:
                    if img_form.cleaned_data.get("DELETE") and img_form.instance.pk:
                        img_form.instance.delete()
                    elif img_form.cleaned_data.get("image"):
                        img_form.save(commit=False)
                        img_form.instance.post = self.object
                        img_form.save()
        return super().form_valid(form)


# DetailView - Представление для отображение одного обьекта
class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(status="pb")
    context_object_name = "post"
    template_name = "posts/detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["comments"] = PostComment.objects.filter(post=self.object)
        context["comment_form"] = CommentForm()
        context["collection_form"] = AddToCollectionForm(user=self.request.user) if self.request.user.is_authenticated else None
        context["collections"] = Collection.objects.filter(user=self.request.user) if self.request.user.is_authenticated else None
        return context


# DeleteView - Представление для удаление обьекта
class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "posts/confirm_delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("post_list")
    success_message = "Пост был успешно удален"


def get_post_user(request: HttpRequest, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    return post, user






# лайков
@login_required  # пользователь должен быть авторизованным
@require_POST  # можно только делать post запрос
def like_post(request: HttpRequest, post_id: int):
    post, user = get_post_user(request, post_id)
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
        if post.dislikes.filter(id=user.id).exists():
            post.dislikes.remove(user)
    return redirect("post_detail", pk=post_id)


# дизлайков
@login_required
@require_POST
def dislike_post(request: HttpRequest, post_id: int):
    post, user = get_post_user(request, post_id)
    if post.dislikes.filter(id=user.id).exists():
        post.dislikes.remove(user)
    else:
        post.dislikes.add(user)
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
    return redirect("post_detail", pk=post_id)


# Написать Изменить Удалить Комментарий
@login_required
@require_POST
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
@require_POST
def change_comment(request: HttpRequest, comment_id: int):
    comment = get_object_or_404(PostComment, id=comment_id)
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid() and comment.user == request.user:
        form.save()
    return redirect("post_detail", pk=comment.post.pk)


@login_required
@require_POST
def delete_comment(request: HttpRequest, comment_id: int):
    comment = get_object_or_404(PostComment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect("post_detail", pk=comment.post.pk)
