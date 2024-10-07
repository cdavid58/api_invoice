# Generated by Django 3.2.8 on 2024-08-20 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0133_alter_employee_psswd'),
        ('inventory', '0016_product_reserved_type_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.employee')),
            ],
        ),
    ]
