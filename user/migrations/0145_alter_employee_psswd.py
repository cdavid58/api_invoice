# Generated by Django 3.2.8 on 2024-09-27 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0144_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='j9DRxO0siHbyGoksq8z8', max_length=20, unique=True),
        ),
    ]
