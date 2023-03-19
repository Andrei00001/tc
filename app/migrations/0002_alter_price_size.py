# Generated by Django 4.1.3 on 2023-03-20 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="size",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="price_size",
                to="app.size",
            ),
        ),
    ]
