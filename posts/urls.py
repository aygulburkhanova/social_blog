from django.urls import path

from posts.views import (
    PostCreateView,
    PostListView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView,
    like_post,
    dislike_post,
    add_comment,
    delete_comment,
    change_comment
)

# path - это функция которая соединяет адрес (URL) с представлением(View)
# path("адрес/", view, name="имя пути")
urlpatterns = [
    # Пост CRUD
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("list/", PostListView.as_view(), name="post_list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),

    # Лайки и Дизлайки
    path("like/<int:post_id>/", like_post, name="like_post"),
    path("dislike/<int:post_id>/", dislike_post, name="dislike_post"),

    # Комментарии
    path("comment/<int:post_id>/create/", add_comment, name="add_comment"),
    path("comment/<int:comment_id>/delete/", delete_comment, name="delete_comment"),
    path("comment/<int:comment_id>/update/", change_comment, name="change_comment")
]
