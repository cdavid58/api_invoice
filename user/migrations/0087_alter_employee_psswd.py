# Generated by Django 3.2.8 on 2024-02-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0086_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='9HVYm1cvh7bFBM7qE8KP', max_length=20, unique=True),
        ),
    ]
