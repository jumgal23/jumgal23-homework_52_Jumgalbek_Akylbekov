# Generated by Django 4.2.7 on 2023-11-28 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=50, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='Время создания'),
        ),
    ]