# Generated by Django 5.2 on 2025-05-04 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS_Marketplace', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS_Marketplace.cart'),
        ),
    ]
