from django.shortcuts import render
from django.views.generic import ListView,  DetailView
from tags.models import Tag

class TagListView(ListView):
    model = Tag
    template_name = "tags/index.html"
    context_object_name = "tag"
    paginate_by = 30
    ordering = ['-created_at']


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"
    context_object_name = "tag"


