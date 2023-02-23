# Generated by Django 4.1.7 on 2023-02-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRM_Data_Staging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('chassis_number', models.CharField(blank=True, max_length=50, null=True)),
                ('vc_number', models.IntegerField(blank=True, null=True)),
                ('engine_type', models.CharField(blank=True, max_length=50, null=True)),
                ('engine', models.IntegerField(blank=True, null=True)),
                ('emission_norm', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_delivered_date', models.DateField(blank=True, null=True)),
                ('lob', models.CharField(blank=True, max_length=50, null=True)),
                ('pl', models.CharField(blank=True, max_length=50, null=True)),
                ('ppl', models.CharField(blank=True, max_length=50, null=True)),
                ('physical_status', models.CharField(blank=True, max_length=50, null=True)),
                ('logical_status', models.CharField(blank=True, max_length=50, null=True)),
                ('dealer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('dealer_code', models.CharField(blank=True, max_length=50, null=True)),
                ('dealer_region', models.CharField(blank=True, max_length=50, null=True)),
                ('dealer_state', models.CharField(blank=True, max_length=50, null=True)),
                ('dealer_city', models.CharField(blank=True, max_length=50, null=True)),
                ('Customer_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_type', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_ph_no', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_state', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_city', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_name', models.CharField(blank=True, max_length=50, null=True)),
                ('driver_contact', models.IntegerField(blank=True, null=True)),
                ('data_received_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'CRM_Data_Staging',
                'managed': True,
            },
        ),
    ]
