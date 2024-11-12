# Generated by Django 5.1.3 on 2024-11-12 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_remove_coupon_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_percent',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
