# Generated by Django 3.2.8 on 2024-09-11 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0141_alter_branch_psswd'),
        ('inventory', '0020_product_percentages'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.branch'),
        ),
    ]
