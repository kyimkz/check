# Generated by Django 5.0.2 on 2024-04-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_cartorderitems_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
