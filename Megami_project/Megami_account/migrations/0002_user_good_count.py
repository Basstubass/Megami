# Generated by Django 4.0.2 on 2022-02-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Megami_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='good_count',
            field=models.IntegerField(default=0),
        ),
    ]
