# Generated by Django 4.0.5 on 2022-12-30 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_book_appoinment_medicines_and_more'),
        ('doctors', '0002_booktime'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation_report',
            name='bookingtable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.book_appoinment'),
        ),
    ]
