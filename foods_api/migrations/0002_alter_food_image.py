# Generated by Django 3.2.9 on 2021-11-18 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]
