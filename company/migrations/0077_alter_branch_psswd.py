# Generated by Django 3.2.8 on 2024-01-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0076_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='wr2C6P9dGZ', max_length=10),
        ),
    ]
