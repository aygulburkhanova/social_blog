"""
Логика Нашего Приложение
"""
from django.views.generic import TemplateView

from collections_app.models import Collection
from posts.models import Post
from tags.models import Tag

from collections_app.forms import AddToCollectionForm

class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(status='pb')
        context["tags"] = Tag.objects.all()
        context["collection_list"]= Collection.objects.all()
        context["collection_form"] = AddToCollectionForm(user=self.request.user) if self.request.user.is_authenticated else None
        context["collections"] = Collection.objects.filter(user=self.request.user) if self.request.user.is_authenticated else None
        return context

