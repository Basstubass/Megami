from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpFrom, ProfileForm, activate_user
from .models import User,Connection

from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.views.generic import View
from .helpers import get_current_user

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

class ProifileDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'detail.html'
    #slug_field = urls.pyに渡すモデルのフィールド名
    slug_field = ('username')
    # urls.pyでのキーワードの名前
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs): # ※(1)
        context = super(ProifileDetail, self).get_context_data(**kwargs)
        username = self.kwargs['username']
        context['username'] = username
        context['user'] = get_current_user(self.request) # ※(2)
        context['following'] = Connection.objects.filter(follower__username=username).count()
        context['follower'] = Connection.objects.filter(following__username=username).count()
        if username is not context['user'].username:
            result = Connection.objects.filter(follower__username=context['user'].username).filter(following__username=username)
            context['connected'] = True if result else False
        return context



# """フォロー"""
def follow_view(request, *args, **kwargs):
    try:
        #request.user.username = ログインユーザーのユーザー名を渡す。
        follower = User.objects.get(username=request.user.username)
        #kwargs['username'] = フォロー対象のユーザー名を渡す。
        following = User.objects.get(username=kwargs['username'])
    #例外処理：もしフォロー対象が存在しない場合、警告文を表示させる。
    except User.DoesNotExist:
        messages.warning(request, '{}は存在しません'.format(kwargs['username']))
        return HttpResponseRedirect(reverse_lazy('home'))
        #フォローしようとしている対象が自分の場合、警告文を表示させる。
    if follower == following:
        messages.warning(request, '自分自身はフォローできません')
    else:
        #フォロー対象をまだフォローしていなければ、DBにフォロワー(自分)×フォロー(相手)という組み合わせで登録する。
        #createdにはTrueが入る
        _, created = Connection.objects.get_or_create(follower=follower, following=following)#（※3）
        #もしcreatedがTrueの場合、フォロー完了のメッセージを表示させる。
        if (created):
            messages.success(request, '{}をフォローしました'.format(following.username))
        #既にフォロー相手をフォローしていた場合、createdにはFalseが入る。
        #フォロー済みのメッセージを表示させる。
        else:
            messages.warning(request, 'あなたはすでに{}をフォローしています'.format(following.username))
    return HttpResponseRedirect(reverse_lazy('detail', kwargs={'username': following.username}))

# """フォロー解除"""
def unfollow_view(request, *args, **kwargs):

    try:
        follower = User.objects.get(username=request.user.username)
        following = User.objects.get(username=kwargs['username'])
        if follower == following:
            messages.warning(request, '自分自身のフォローを外せません')
        else:
            unfollow = Connection.objects.get(follower=follower, following=following)
            #フォロワー(自分)×フォロー(相手)という組み合わせを削除する。
            unfollow.delete()
            messages.success(request, 'あなたは{}のフォローを外しました'.format(following.username))
    except User.DoesNotExist:
        messages.warning(request, '{}は存在しません'.format(kwargs['username']))
        return HttpResponseRedirect(reverse_lazy('home'))
    except Connection.DoesNotExist:
        messages.warning(request, 'あなたは{0}をフォローしませんでした'.format(following.username))

    return HttpResponseRedirect(reverse_lazy('detail', kwargs={'username': following.username}))








