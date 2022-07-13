# Generated by Django 4.0.1 on 2022-03-31 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mart_python', '0008_deatiledorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='deatiledorder',
            name='customerId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.CharField(default=-10, max_length=500),
            preserve_default=False,
        ),
    ]