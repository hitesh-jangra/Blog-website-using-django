# Generated by Django 2.2.3 on 2019-07-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20190711_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='field',
            field=models.SlugField(default=True),
        ),
    ]
