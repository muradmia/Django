# Generated by Django 5.0.1 on 2024-04-09 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_user_father'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('fathername', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=15)),
            ],
        ),
    ]