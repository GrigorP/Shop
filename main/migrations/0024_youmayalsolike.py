# Generated by Django 4.2.6 on 2023-10-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_leavereview_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouMayAlsoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='main.product')),
            ],
        ),
    ]
