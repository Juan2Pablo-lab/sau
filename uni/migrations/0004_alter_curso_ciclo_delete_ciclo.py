# Generated by Django 5.0.6 on 2024-06-14 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uni", "0003_alter_ciclo_nombre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="ciclo",
            field=models.CharField(
                choices=[
                    ("1", "Primer Ciclo"),
                    ("2", "Segundo Ciclo"),
                    ("3", "Tercer Ciclo"),
                    ("4", "Cuarto Ciclo"),
                    ("5", "Quinto Ciclo"),
                    ("6", "Sexto Ciclo"),
                    ("7", "Septimo Ciclo"),
                    ("8", "Octavo Ciclo"),
                    ("9", "Noveno Ciclo"),
                    ("10", "Decimo Ciclo"),
                ],
                max_length=5,
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="Ciclo",
        ),
    ]