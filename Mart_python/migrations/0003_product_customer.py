# Generated by Django 4.0.1 on 2022-03-13 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mart_python', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Mart_python.registration'),
            preserve_default=False,
        ),
    ]
