# Generated by Django 4.1.1 on 2022-10-05 22:52

from django.db import migrations, models
import django.db.models.deletion
import main_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Категорії',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_special', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField()),
                ('ingredients', models.CharField(max_length=300)),
                ('desc', models.TextField(blank=True, max_length=1000)),
                ('photo', models.ImageField(upload_to=main_page.models.Dish.get_file_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.category')),
            ],
            options={
                'verbose_name': 'Страви',
                'ordering': ('position',),
            },
        ),
    ]
