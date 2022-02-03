from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import activate_user
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpFrom, UserChangeForm
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


class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'registration/change.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'username' : self.request.user.username,
            'icon' : self.request.user.icon,
            'introduction' : self.request.user.introduction,
        })
        return kwargs