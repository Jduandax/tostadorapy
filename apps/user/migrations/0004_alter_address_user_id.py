# Generated by Django 4.1.5 on 2023-01-31 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
