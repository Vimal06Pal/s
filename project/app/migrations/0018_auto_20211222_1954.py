# Generated by Django 3.2.8 on 2021-12-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20211222_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
