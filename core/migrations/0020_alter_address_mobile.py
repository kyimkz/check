# Generated by Django 5.0.3 on 2024-04-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_address_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='mobile',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
