# Generated by Django 4.2.4 on 2023-08-18 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="history",
            name="content_type",
        ),
        migrations.RemoveField(
            model_name="history",
            name="object_id",
        ),
        migrations.AddField(
            model_name="history",
            name="urls",
            field=models.URLField(default="www.google.com"),
        ),
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 18, 22, 37, 34, 936672)
            ),
        ),
    ]
