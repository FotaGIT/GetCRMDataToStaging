# Generated by Django 4.1.7 on 2023-03-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_crm', '0009_exceptiongetcrmdatatostaging_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='exceptiongetcrmdatatostaging',
            name='payload',
            field=models.TextField(blank=True, null=True),
        ),
    ]