# Generated by Django 5.1.3 on 2024-11-12 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='shipping',
        ),
    ]
