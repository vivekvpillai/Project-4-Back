# Generated by Django 3.2.9 on 2021-11-19 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foods_api', '0002_alter_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
