# Generated by Django 4.1.5 on 2023-01-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='presentation',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
