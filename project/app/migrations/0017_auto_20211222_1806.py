# Generated by Django 3.2.8 on 2021-12-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20211222_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]