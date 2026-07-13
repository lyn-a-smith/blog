from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    PostDetailView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_new'),
]
