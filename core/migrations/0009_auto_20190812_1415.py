# Generated by Django 2.2.3 on 2019-08-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]