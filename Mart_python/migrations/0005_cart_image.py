# Generated by Django 4.0.1 on 2022-03-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mart_python', '0004_cart_alter_registration_mobileno'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
