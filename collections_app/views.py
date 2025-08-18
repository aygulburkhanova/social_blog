from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,  DetailView, DeleteView
from collections_app.models import Collection

class CollectionListView(ListView):
    model = Collection
    template_name = "collection_app/index.html"
    paginate_by = 30
    context_object_name = "collections"
    ordering = ['-created_at']


class CollectionCreateView(SuccessMessageMixin, CreateView):
    model = Collection
    template_name = "collection_app/form.html"
    success_url = reverse_lazy("collections_list")
    success_message = "Колекция был успешно создан "


class CollectionUpdateView(SuccessMessageMixin, UpdateView):
    model = Collection
    template_name = "collection_app/form.html"
    success_url = reverse_lazy("collections_list")
    success_message = "Колекция был успешно обновлен "
    pk_url_kwarge = "pk"


class CollectionDetailView(DetailView):
    model = Collection
    context_object_name = "collection"
    template_name = "collection_app/detail.html"



class CollectionDeleteView(SuccessMessageMixin, DeleteView):
    model = Collection
    template_name = "collection_app/detail.html"
    context_object_name = "collection"
    success_url = reverse_lazy("collections_list")
    success_message = "Колекция был успешно удален"



