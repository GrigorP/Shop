# Generated by Django 4.1.4 on 2023-11-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_leavereview_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavereview',
            name='rating',
            field=models.IntegerField(null=True, verbose_name='Rating'),
        ),
    ]