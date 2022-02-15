# from django.views.generic import TemplateView,ListView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
from .models import Post
from Megami_account.models import  Connection
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.http import JsonResponse
from django.views.generic.edit import CreateView

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        action = request.GET.get('action')
        if action == "new":
            post_data = Post.objects.order_by('-id')
        else: 
            post_data = Post.objects.order_by('-good_count')
        user_follower = Connection.objects.filter(following=user.id).all()
        user_following = Connection.objects.filter(follower=user.id).all()
        return render(request, 'home.html',{
            'post_data':post_data,
            'user_follower':user_follower,
            'user_following':user_following
        })


# class VoteView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):






class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'post_detail.html',{
            'post_data': post_data
        })

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        return render(request, 'post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.user = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image') # 追加
            post_data.save()
            
            return redirect('Megami_app:post_detail', post_data.id)

        return render(request, 'post_form.html', {
            'form': form
        })


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial={
                'title': post_data.title,
                'content': post_data.content,
                'image': post_data.image, # 追加
            }
        )
        return render(request, 'post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            if request.FILES:
                post_data.image = request.FILES.get('image') # 追加
            post_data.save()
            return redirect('Megami_app:post_detail', self.kwargs['pk'])
        return render(request, 'post_form.html', {
            'form': form
        })

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'post_delete.html',{
            'post_data': post_data
        })
    
    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('home')
    

# テスト
# class ArticleCreateView(CreateView):
#     model = Post
#     fields = ('title', )
    
#     def get_success_url(self):
#         return reverse('article:article_list')

def add_good_count_for_article(request):
    article_id = request.POST.get('id')
    article = Post.objects.get(id=article_id)

    article.good_count += 1
    article.save()
    data = {
        'id': article_id,
        'good_count': article.good_count,
    }
    return JsonResponse(data)


def chat( request ):
    return render( request, '' )