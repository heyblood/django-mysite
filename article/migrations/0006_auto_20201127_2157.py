# Generated by Django 2.2 on 2020-11-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20201127_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='栏目名称'),
        ),
    ]