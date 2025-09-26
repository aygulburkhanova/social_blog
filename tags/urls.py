from django.urls import path

from tags.views import TagListView, TagDetailView
urlpatterns = [
    path("list/", TagListView.as_view(), name="tag_list"),
    path("detail/<int:pk>", TagDetailView.as_view(), name="tag_detail"),
]