# Generated by Django 5.0.6 on 2024-07-07 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_customer_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='account_holder_name',
        ),
    ]
