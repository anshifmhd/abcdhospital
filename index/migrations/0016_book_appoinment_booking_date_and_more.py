# Generated by Django 4.0.5 on 2022-12-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_appoinment',
            name='booking_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='book_appoinment',
            name='booking_time',
            field=models.TimeField(null=True),
        ),
    ]