"""Megami_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from Megami_app import views
from Megami_account import views

from django.conf import settings
from django.conf.urls.static import static




home_view = TemplateView.as_view(template_name = "home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Megami_app.urls')),
    path('', login_required(home_view), name="home"),
    path('', include('django.contrib.auth.urls')),

    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name="activate"),
    path('change/', views.ProfileEditView.as_view(), name="change"),

    # path('post/<int:pk>',views.PostDetailView.as_view(), name="post_detail")
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)