# Generated by Django 3.2.8 on 2021-12-09 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_addcarousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='multiple_images',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
    ]