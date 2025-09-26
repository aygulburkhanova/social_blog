from django.views.generic import ListView, DetailView

from posts.models import Post
from tags.models import Tag


class TagListView(ListView):
    model = Tag
    template_name = "tags/index.html"
    context_object_name = "tags"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"
    context_object_name = "tag"

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(tags__in=[self.object])
        return context