# Generated by Django 3.2.18 on 2023-12-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_minhaeiro', '0006_remove_expense_expense_type_creditcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='pay_day',
            field=models.DateField(),
        ),
    ]