# Generated by Django 4.0.5 on 2022-11-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_department'),
        ('index', '0002_rename_username_register_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.add_doc')),
            ],
        ),
    ]