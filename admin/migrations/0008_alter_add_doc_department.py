# Generated by Django 4.0.5 on 2022-11-30 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0007_remove_add_doc_deprmt_add_doc_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_doc',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin.department'),
        ),
    ]
