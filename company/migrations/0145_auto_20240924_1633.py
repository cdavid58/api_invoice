# Generated by Django 3.2.8 on 2024-09-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0144_auto_20240923_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='bale',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='quantity',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='unit',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='qqGQ6ovaNk', max_length=30),
        ),
    ]
