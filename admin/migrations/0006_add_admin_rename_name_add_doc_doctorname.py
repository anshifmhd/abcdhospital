# Generated by Django 4.0.5 on 2022-11-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0005_remove_add_doc_password_remove_add_doc_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='add_doc',
            old_name='name',
            new_name='doctorName',
        ),
    ]
