# Generated by Django 4.2.6 on 2023-11-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="movies",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("m_name", models.CharField(max_length=30)),
                ("release_year", models.IntegerField()),
                ("genre", models.CharField(default="action", max_length=20)),
                ("language", models.CharField(default="en", max_length=20)),
                ("rating", models.IntegerField()),
                ("portrait", models.URLField()),
                ("landscape", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="userinputs",
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
                ("m_name", models.CharField(max_length=50)),
                ("u_name", models.CharField(max_length=30)),
                ("review", models.CharField(max_length=500)),
                ("rating", models.IntegerField()),
            ],
        ),
    ]
