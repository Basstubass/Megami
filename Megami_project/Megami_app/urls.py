from django.urls import path
from .views import IndexView, HomeView, SignView, ConfView, re_login

urlpatterns = [
    path('', IndexView.as_view()),
    path('home/', HomeView.as_view()),
    path('signin/', SignView.as_view()),
    path('conf/', ConfView.as_view()),
    path('re_login/',re_login.as_view()),

]