# Generated by Django 4.2.7 on 2023-12-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_remove_article_updated_at_article_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default=1, max_length=3000, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='подробное описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
