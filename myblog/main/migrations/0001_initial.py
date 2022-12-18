# Generated by Django 4.1.3 on 2022-12-18 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=155)),
                ('is_published', models.BooleanField(default=None)),
                ('published_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='main.comments')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default.png', upload_to='profile/')),
                ('bio', models.TextField()),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.posts')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.rating'),
        ),
        migrations.AddField(
            model_name='posts',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='commentator_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.posts'),
        ),
    ]
