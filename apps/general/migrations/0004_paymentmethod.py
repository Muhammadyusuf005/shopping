# Generated by Django 5.1.3 on 2024-11-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_alter_general_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=47, unique=True)),
            ],
        ),
    ]
