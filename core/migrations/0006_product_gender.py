# Generated by Django 5.0.2 on 2024-03-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_productreview_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(default='Female', max_length=100),
        ),
    ]
