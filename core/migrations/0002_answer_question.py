# Generated by Django 2.2.3 on 2019-07-17 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='core.Question'),
        ),
    ]
