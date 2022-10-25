from django.db import models
import uuid
import os

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=40, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name}: {self.position}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('position', )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    ingredients = models.CharField(max_length=300)
    desc = models.TextField(max_length=1_000, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name}: {self.name}: {self.position}'

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ('position', )


class Gallery(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)


class Whyus(models.Model):

    number = models.SmallIntegerField(unique=True, verbose_name="Number")
    name = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Why us'
        verbose_name_plural = 'Why us'
        ordering = ('number', )


class Events(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/events/', filename)

    item = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField(verbose_name="Event price")
    description = models.TextField(max_length=1_000, blank=False)
    subtitle1 = models.TextField(blank=True, verbose_name="sub1")
    subtitle2 = models.TextField(blank=True, verbose_name="sub2")
    subtitle3 = models.TextField(blank=True, verbose_name="sub3")
    aftertitle = models.TextField(blank=True, verbose_name="After text")
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def str(self):
        return f'{self.item}: {self.price}'

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class HeroSec(models.Model):
    def get_file_name(self, filename):
        tmp = filename.strip().split('.')[-1]
        filename = f"{uuid.uuid4()}.{tmp}"
        return os.path.join('images/gallery/', filename)

    name = models.CharField(max_length=30, verbose_name="name")
    info = models.TextField(verbose_name="info")
    photo = models.ImageField(upload_to=get_file_name, verbose_name="photos")
    is_visible = models.BooleanField(default=True, verbose_name="is_visible")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hero_Section"
        verbose_name_plural = "Hero_Section"


