# Generated by Django 3.1.7 on 2021-02-28 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=6)),
                ('order', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('active', models.BooleanField()),
                ('tasklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tasklist')),
            ],
        ),
    ]