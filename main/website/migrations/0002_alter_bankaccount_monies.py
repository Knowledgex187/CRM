# Generated by Django 5.0.6 on 2024-07-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='monies',
            field=models.IntegerField(),
        ),
    ]
