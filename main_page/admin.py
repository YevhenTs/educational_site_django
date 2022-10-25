from django.contrib import admin
from .models import Dish, Category, Gallery, Whyus, Events, HeroSec

# Register your models here.
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Whyus)
admin.site.register(Events)
admin.site.register(HeroSec)