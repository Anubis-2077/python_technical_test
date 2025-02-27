# Generated by Django 4.1 on 2024-09-02 23:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("passenger", "0001_initial"),
        ("driver", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("origin", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                (
                    "destination",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                ("distance", models.FloatField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("in_course", "In course"),
                            ("finished", "Finished"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("begin_time", models.DateTimeField(null=True)),
                ("finish_time", models.DateTimeField(null=True)),
                ("duration", models.TimeField(null=True)),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="driver.driver"
                    ),
                ),
                (
                    "passenger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="passenger.passenger",
                    ),
                ),
            ],
        ),
    ]
