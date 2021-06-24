# Generated by Django 2.2 on 2021-06-24 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0016_remove_articlepost_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_time', models.DateTimeField(auto_now=True, verbose_name='收藏时间')),
                ('artcle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticlePost', verbose_name='收藏文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='收藏用户')),
            ],
            options={
                'verbose_name': '文章收藏',
                'verbose_name_plural': '文章收藏',
                'db_table': 'tb_article_collect',
                'ordering': ('-collected_time',),
            },
        ),
    ]
