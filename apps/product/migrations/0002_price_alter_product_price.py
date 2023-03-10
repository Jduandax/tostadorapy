# Generated by Django 4.1.5 on 2023-01-31 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('presentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.presentation')),
            ],
            options={
                'db_table': 'tostadora_product_price',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.price'),
        ),
    ]
