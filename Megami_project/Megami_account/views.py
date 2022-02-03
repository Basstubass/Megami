from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import activate_user

from .forms import SignUpFrom
# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpFrom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)