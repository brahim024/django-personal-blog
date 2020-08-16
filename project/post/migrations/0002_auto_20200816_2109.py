# Generated by Django 3.0.6 on 2020-08-16 19:09

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=post.models.image_upload),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='desciptions',
            field=models.TextField(max_length=50),
        ),
    ]