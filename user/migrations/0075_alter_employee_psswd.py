# Generated by Django 3.2.8 on 2024-01-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0074_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='ZU2SYE62lhHsx7hLQhHr', max_length=20, unique=True),
        ),
    ]
