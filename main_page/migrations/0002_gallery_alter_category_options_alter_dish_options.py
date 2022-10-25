# Generated by Django 4.1.1 on 2022-10-12 22:22

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=main_page.models.Gallery.get_file_name)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('position',), 'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
    ]