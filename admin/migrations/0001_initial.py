# Generated by Django 4.0.5 on 2022-10-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('deprmt', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('quali', models.CharField(max_length=100)),
            ],
        ),
    ]
