# Generated by Django 3.2.8 on 2024-02-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_best_selling_product_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_product',
            name='modified_values',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
