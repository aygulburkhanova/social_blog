from django.urls import path

from collections_app.views import add_to_collection, CollectionCreateView, CollectionListView, CollectionDeleteView, \
    CollectionDetailView, CollectionUpdateView, UserCollectionListView

urlpatterns = [
    path('add/<int:post_id>', add_to_collection, name='add_to_collection'),
    path('create/', CollectionCreateView.as_view(), name='collection_create'),
    path('update/<int:pk>', CollectionUpdateView.as_view(), name='collection_update'),
    path('list/', CollectionListView.as_view(), name='collection_list'),
    path('detail/<int:pk>', CollectionDetailView.as_view(), name='collection_detail'),
    path('delete/<int:pk>', CollectionDeleteView.as_view(), name='collection_delete'),
]
