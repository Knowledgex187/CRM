# Generated by Django 5.0.6 on 2024-07-07 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_bankaccount_account_holder_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='ifsc_code',
        ),
    ]
