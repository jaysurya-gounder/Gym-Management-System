# Generated by Django 3.1.5 on 2021-03-01 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0030_auto_20210301_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_master',
            name='user_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
