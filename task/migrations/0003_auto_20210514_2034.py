# Generated by Django 3.2 on 2021-05-14 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_remove_todolist_memo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['complete']},
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='task',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='estimated_time',
        ),
        migrations.AddField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='디테일'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='완료여부'),
        ),
    ]