# Generated by Django 5.0.1 on 2024-04-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('mother', models.CharField(max_length=20)),
            ],
        ),
    ]