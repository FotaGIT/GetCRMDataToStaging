# Generated by Django 4.0.4 on 2023-02-22 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crm_data_staging',
            old_name='Customer_Name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='crm_data_staging',
            old_name='engine',
            new_name='engine_number',
        ),
    ]
