from django.urls import path
from .views import reservation_list, reservation_update

app_name = 'manager'

urlpatterns = [
    path('reservation/', reservation_list, name='reservation_list'),
    path('reservation/update/<int:pk>', reservation_update, name='reservation_close')
]


