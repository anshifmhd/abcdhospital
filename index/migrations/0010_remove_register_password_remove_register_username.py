# Generated by Django 4.0.5 on 2022-11-29 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_alter_register_email_alter_register_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='userName',
        ),
    ]
