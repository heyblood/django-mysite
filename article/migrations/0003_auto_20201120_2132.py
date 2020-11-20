# Generated by Django 2.2 on 2020-11-20 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlepost_total_views'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-created',), 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='total_views',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterModelTable(
            name='articlepost',
            table='tb_article',
        ),
    ]
