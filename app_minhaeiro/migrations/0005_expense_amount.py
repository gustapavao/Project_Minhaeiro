# Generated by Django 3.2.18 on 2023-12-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_minhaeiro', '0004_auto_20231228_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
