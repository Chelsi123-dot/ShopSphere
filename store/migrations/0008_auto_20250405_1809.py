# Generated by Django 3.1 on 2025-04-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
