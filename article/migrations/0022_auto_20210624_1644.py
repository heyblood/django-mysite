# Generated by Django 2.2 on 2021-06-24 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0021_auto_20210624_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecollect',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticlePost', unique=True, verbose_name='收藏文章'),
        ),
    ]