# Generated by Django 4.0.5 on 2022-11-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_alter_register_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userName',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
