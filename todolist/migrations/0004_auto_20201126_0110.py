# Generated by Django 3.1.2 on 2020-11-26 01:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0003_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entry',
            new_name='Todo',
        ),
    ]