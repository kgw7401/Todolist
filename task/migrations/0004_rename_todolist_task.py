# Generated by Django 3.2 on 2021-05-17 22:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_auto_20210514_2034'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoList',
            new_name='Task',
        ),
    ]
