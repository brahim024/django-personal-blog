# Generated by Django 3.0.6 on 2020-08-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20200812_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='adress',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]