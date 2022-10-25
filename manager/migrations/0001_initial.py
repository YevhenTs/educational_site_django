# Generated by Django 4.1.1 on 2022-10-16 16:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('persons', models.PositiveSmallIntegerField()),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Wrong phone number', regex='^(\\d{3}[- ,]?){2}\\d{4}$')])),
                ('message', models.TextField(max_length=500)),
                ('is_processed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Wrong phone number', regex='^(\\d{3}[- ,]?){2}\\d{4}$')])),
                ('message', models.TextField(max_length=500)),
                ('is_processed', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
