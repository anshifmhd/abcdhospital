# Generated by Django 4.0.5 on 2022-12-11 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_rename_user_id_book_appoinment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book_appoinment',
            old_name='user',
            new_name='user_id',
        ),
    ]