# Generated by Django 5.0.4 on 2024-04-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('roll', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('FatherName', models.CharField(max_length=15)),
                ('MotherName', models.CharField(max_length=15)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]