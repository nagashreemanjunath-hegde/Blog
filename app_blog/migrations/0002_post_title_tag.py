# Generated by Django 4.0.2 on 2022-03-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='This is the blog', max_length=255),
        ),
    ]
