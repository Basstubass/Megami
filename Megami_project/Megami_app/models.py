from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

## 投稿モデル
class Post(models.Model):
   title = models.CharField('タイトル', max_length=50)
   content = models.TextField('本文')
   image = models.ImageField('画像', upload_to='images', blank=True)
   created_at = models.DateTimeField('投稿日', default=timezone.now)
   user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   good_count = models.IntegerField(default=0)

   def __str__(self):
       return self.title



