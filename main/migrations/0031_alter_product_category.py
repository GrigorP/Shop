# Generated by Django 4.2.6 on 2023-10-30 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0030_auto_20231030_1934"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.category"
            ),
        ),
    ]
