# Generated by Django 3.2.9 on 2021-11-19 17:34

import django.contrib.postgres.fields
from django.db import migrations, models
import useracc_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('useracc_api', '0007_alter_user_user_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_foods',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=useracc_api.models.getfoods, size=None),
        ),
    ]
