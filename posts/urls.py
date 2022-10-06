from django.urls import path
from .views import (
    PostListView,
    ArchivedPostListView,
    PublishedPostListView,
    DraftPostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)


urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('published/', PublishedPostListView.as_view(), name='published_list'),
    path('archived/', ArchivedPostListView.as_view(), name='archived_list'),
    path('drafts/', DraftPostListView.as_view(), name='draft_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]