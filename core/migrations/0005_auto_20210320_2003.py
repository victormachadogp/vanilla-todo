# Generated by Django 3.1.7 on 2021-03-20 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210304_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
