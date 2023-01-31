# Generated by Django 4.1.5 on 2023-01-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_price_presentation_price_delete_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='price',
        ),
        migrations.AddField(
            model_name='presentation',
            name='price_presentation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
