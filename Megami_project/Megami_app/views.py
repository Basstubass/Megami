# from django.views.generic import TemplateView,ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
# from .models import Post

# class IndexView(TemplateView):
#     template_name = "index.html"
#     def login(self, request):
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             login(request, user)
            
#             return HttpResponseRedirect(reverse('/'))
#         return render(request, 'login.html')

# class HomeView(TemplateView):
#     template_name = 'home.html'
    # def get_queryset(self):
    #     """Return Schools """
    #     return models.School.objects.order_by('id')
    
# class SignView(TemplateView):
#     template_name = "signin.html"
# class ConfView(TemplateView):
#     template_name = "conf.html"
# class re_login(TemplateView):
#     template_name = "re_login.html"
# class logout(TemplateView):
#     template_name = "logout.html"