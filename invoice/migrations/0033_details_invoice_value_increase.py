# Generated by Django 3.2.8 on 2024-10-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0032_merge_0031_auto_20240918_1749_0031_auto_20240918_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='details_invoice',
            name='value_increase',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
