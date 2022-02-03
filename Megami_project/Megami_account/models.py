from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    icon = models.ImageField(upload_to='img/',verbose_name='アイコン',blank=True,)
    introduction = models.CharField(max_length=150, blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True, symmetrical=False)
