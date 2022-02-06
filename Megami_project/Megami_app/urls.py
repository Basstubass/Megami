from django.urls import path
# from .views import IndexView
from django.contrib.auth import authenticate, login

from django.urls import path
from django import views
from .views import PostDetailView, CreatePostView
from Megami_app import views
## アプリケーション名
app_name = 'Megami_app'
## URLのパターンを定義するためのもの
urlpatterns = [
    path('',views.IndexView.as_view(), name='home'),
    path('post/<int:pk>/' ,views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/' ,views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/' ,views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/' ,views.PostDeleteView.as_view(), name='post_delete'),

]