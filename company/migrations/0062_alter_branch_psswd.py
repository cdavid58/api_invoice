# Generated by Django 3.2.8 on 2024-01-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0061_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='NcBYnUaLCE', max_length=10),
        ),
    ]
