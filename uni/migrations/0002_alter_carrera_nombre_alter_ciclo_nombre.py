# Generated by Django 5.0.6 on 2024-06-14 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uni", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carrera",
            name="nombre",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="ciclo",
            name="nombre",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
