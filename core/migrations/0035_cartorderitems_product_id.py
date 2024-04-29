# Generated by Django 5.0.2 on 2024-04-23 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_cartorderitems_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
