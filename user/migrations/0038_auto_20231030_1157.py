# Generated by Django 3.2.8 on 2023-10-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0037_alter_employee_psswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='StmPZsiXRCYOrIXbHhVx', max_length=20, unique=True),
        ),
    ]
