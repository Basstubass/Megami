from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpFrom, ProfileForm, activate_user
from .models import User
from django.views.generic import View



from Megami_app.models import Post
from Megami_app.forms import PostForm

# Create your views here
class SignUpView(CreateView):
    form_class = SignUpFrom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)



class ProfileEditView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        user_data = User.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'username' : user_data.username,
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'description': user_data.description,
                'image': user_data.image
            }
        )
        return render(request, 'registration/change.html', {
            'form': form,
            'user_data': user_data
        })

    def post(self, request, *args, **kwargs):
        # post_data = Post.objects.order_by('-id')
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = User.objects.get(id=request.user.id)
            user_data.username = form.cleaned_data['username']
            user_data.first_name = form.cleaned_data['first_name']
            user_data.last_name = form.cleaned_data['last_name']
            user_data.description = form.cleaned_data['description']
            if request.FILES.get('image'):
                user_data.image = request.FILES.get('image')
            user_data.save()
            return redirect('home')

        return render('templates/home.html', {
            'form': form,
            # 'post_data':post_data
        })
    

    # def get(self, request, *args, **kwargs):
    #     post_data = Post.objects.order_by('-id')
    #     return render(request, 'index.html',{
    #         'post_data':post_data
    #     })