# Generated by Django 4.2.6 on 2023-11-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_color_size_product_color_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(to='main.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='main.size'),
        ),
    ]
