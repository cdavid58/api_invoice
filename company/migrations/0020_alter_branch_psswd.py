# Generated by Django 3.2.8 on 2023-10-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0019_auto_20231011_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='zKjRoqM9zL', max_length=10),
        ),
    ]
