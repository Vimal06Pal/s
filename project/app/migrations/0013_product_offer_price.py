# Generated by Django 3.2.8 on 2021-12-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_price',
            field=models.IntegerField(default=0),
        ),
    ]
