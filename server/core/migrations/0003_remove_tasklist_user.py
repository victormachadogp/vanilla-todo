# Generated by Django 3.1.7 on 2021-02-28 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_task_tasklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='user',
        ),
    ]
