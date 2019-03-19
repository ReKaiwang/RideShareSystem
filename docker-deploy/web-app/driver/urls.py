from django.urls import path

from . import views
from  users import urls

urlpatterns = [
    path('find_ride/',views.find_ride, name = 'findride'),
    path('ridestatus/', views.ride_view, name ='drivestatus')
]