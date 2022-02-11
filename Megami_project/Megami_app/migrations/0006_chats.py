# Generated by Django 4.0.2 on 2022-02-09 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Megami_app', '0005_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=250, verbose_name='message')),
                ('catchuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catchuser', to=settings.AUTH_USER_MODEL)),
                ('senduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]