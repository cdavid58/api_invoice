# Generated by Django 3.2.8 on 2024-09-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0139_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='NLgowFE9nCnNdTcsN3fR', max_length=20, unique=True),
        ),
    ]
