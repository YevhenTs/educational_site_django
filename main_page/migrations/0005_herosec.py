# Generated by Django 4.1.1 on 2022-10-24 22:47

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('info', models.TextField(verbose_name='info')),
                ('photo', models.ImageField(upload_to=main_page.models.HeroSec.get_file_name, verbose_name='photos')),
                ('is_visible', models.BooleanField(default=True, verbose_name='is_visible')),
            ],
            options={
                'verbose_name': 'Hero_Section',
                'verbose_name_plural': 'Hero_Section',
            },
        ),
    ]
