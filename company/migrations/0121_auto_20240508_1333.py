# Generated by Django 3.2.8 on 2024-05-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0120_alter_branch_psswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='consumption_tax',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='szIlCpZsa9', max_length=10),
        ),
    ]
