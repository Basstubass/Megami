from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django import forms
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


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=20, label='ユーザーネーム')
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False, )
