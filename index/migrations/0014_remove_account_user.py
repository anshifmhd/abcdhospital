# Generated by Django 4.0.5 on 2022-12-08 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_alter_account_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]