# Generated by Django 3.1.5 on 2021-02-27 06:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zulfiapp', '0010_auto_20210227_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 27, 6, 11, 50, 719288, tzinfo=utc)),
        ),
    ]