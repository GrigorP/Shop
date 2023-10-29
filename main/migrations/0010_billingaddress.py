# Generated by Django 4.2.6 on 2023-10-27 08:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_ourshop_prodcuts_ourshop_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=254, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('AddressLine1', models.CharField(max_length=254, verbose_name='AddressLine1')),
                ('AddressLine2', models.CharField(max_length=254, verbose_name='AddressLine2')),
                ('city', models.CharField(max_length=254, verbose_name='City')),
                ('state', models.CharField(max_length=254, verbose_name='State')),
                ('zipcode', models.PositiveIntegerField(verbose_name='Zip Code')),
            ],
            options={
                'verbose_name': 'BillingAddress',
                'verbose_name_plural': 'BillingAddresses',
            },
        ),
    ]
