from django.shortcuts import render, redirect
from .models import Category, Dish, Gallery, Whyus, Events, HeroSec
from .forms import UserReservationsForm


# Create your views here.


def main_page_view(request):
    if request.method == 'POST':
        user_reservation = UserReservationsForm(request.POST)
        if user_reservation.is_valid():
            user_reservation.save()
            return redirect('/')
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True).filter(is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True).filter(is_special=True)
    gallery = Gallery.objects.filter(is_visible=True)
    user_reservation = UserReservationsForm()
    whyus = Whyus.objects.all()
    events = Events.objects.filter(is_visible=True)
    hero_sec = HeroSec.objects.filter(is_visible=True)

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'gallery': gallery,
        'form_reservation': user_reservation,
        'whyus': whyus,
        'events': events,
        'hero_sec': hero_sec
    })