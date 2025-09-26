from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from collections_app.forms import AddToCollectionForm, CollectionForm
from collections_app.models import Collection, CollectionItems
from posts.models import Post


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_app/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_app/form.html'
    success_url = reverse_lazy('index')


class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Collection
    success_url = reverse_lazy('index')
    template_name = 'collections_app/confirm_delete.html'


class CollectionListView(ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = 'collections_app/index.html'
    paginate_by = 50  # Пагинация
    ordering = ['-created_at']  # Сортировка


class UserCollectionListView(CollectionListView):
    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)


class CollectionDetailView(DetailView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collections_app/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        collection_items = self.object.collection_items.all()
        context["posts"] = [item.post for item in collection_items]
        return context


@login_required
@require_POST
def add_to_collection(request: HttpRequest, post_id: int):
    form = AddToCollectionForm(request.user, request.POST)

    if form.is_valid():
        collection = form.cleaned_data["collections"]
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        CollectionItems.objects.create(collection=collection, post=post, user=user)
    next_url = request.POST.get('next', 'index')
    return redirect(next_url)
