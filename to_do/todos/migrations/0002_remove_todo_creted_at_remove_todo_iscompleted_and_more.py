# Generated by Django 4.1 on 2023-06-02 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='creted_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='iscompleted',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='todo',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]