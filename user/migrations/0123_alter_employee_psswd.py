# Generated by Django 3.2.8 on 2024-05-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0122_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='e9J73QK0wsfrARlurnT3', max_length=20, unique=True),
        ),
    ]
