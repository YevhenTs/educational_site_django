# Generated by Django 4.1.1 on 2022-10-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_gallery_alter_category_options_alter_dish_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whyus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(unique=True, verbose_name='Number')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('desc', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Why us',
                'verbose_name_plural': 'Why us',
                'ordering': ('number',),
            },
        ),
    ]
