import django_filters
from django import forms
from django.db.models.aggregates import Count

from posts.models import Post
from tags.models import Tag


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    tags = django_filters.ModelChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.Select(attrs={'class': "tags"}),
        empty_label="Все",
    )
    sort = django_filters.OrderingFilter(
        label="Сортировка",
        choices=(
            ("new", "Новые"),
            ("popular", "Популярные"),
            ("comments", "Обсуждаемые")
        ),
        method="filter_by_order"
    )

    class Meta:
        model = Post
        fields = ["tags", "title", "sort"]

    def filter_by_order(self, queryset, name, value):
        if not value:
            return queryset
        sort_value = value[0]
        if sort_value == "new":
            return queryset.order_by("-created_at")
        elif sort_value == "popular":
            return queryset.annotate(num_likes=Count("likes")).order_by("-num_likes")
        elif sort_value == "comments":
            return queryset.annotate(num_comments=Count("comments")).order_by("-num_comments")
        return queryset