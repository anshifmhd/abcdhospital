# Generated by Django 4.0.5 on 2022-12-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0010_add_doc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_doc',
            name='image',
            field=models.ImageField(null=True, upload_to='doctors/static/images'),
        ),
    ]
