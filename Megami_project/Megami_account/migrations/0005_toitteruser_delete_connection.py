# Generated by Django 4.0.2 on 2022-02-08 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Megami_account', '0004_connection'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToitterUser',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('following', models.ManyToManyField(blank=True, related_name='followed_by', to='Megami_account.ToitterUser')),
            ],
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
    ]
