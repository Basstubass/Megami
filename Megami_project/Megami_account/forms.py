from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.forms import ModelForm
from django.contrib.auth.models import User

User = get_user_model()

subject = "登録確認メール"
message_template = """
    登録ありがとうございます。
    本登録は以下のURLをクリックしてください。
    """

def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "activate/{}/{}/".format(uid, token)



class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        user.is_active = False

        if commit:
            user.save()
            activate_url = get_activate_url(user)
            message = message_template + activate_url
            user.email_user(subject, message)
        return user

def activate_user(uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False
    
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True

    return False

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'icon',
            'introduction',
        ]
    
    def __init__(self, username=None, icon=None, introduction=None,  *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if username:
            self.fields['username'].widget.attrs['value'] = username
        if icon:
            self.fields['icon'].widget.attrs['value'] = icon
        if introduction:
            self.fields['introduction'].widget.attrs['value'] = introduction
    
    def update(self, user):
        user.username = self.cleaned_data['username']
        user.icon = self.cleaned_data['icon']
        user.introduction = self.cleaned_data['introduction']
        user.save()
