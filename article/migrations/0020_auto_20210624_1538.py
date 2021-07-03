# Generated by Django 2.2 on 2021-06-24 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20210624_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecollect',
            options={'ordering': ('-collected_time',), 'verbose_name': '收藏管理', 'verbose_name_plural': '收藏管理'},
        ),
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-created',), 'verbose_name': '文章管理', 'verbose_name_plural': '文章管理'},
        ),
        migrations.RenameField(
            model_name='articlecollect',
            old_name='artcle',
            new_name='article',
        ),
    ]