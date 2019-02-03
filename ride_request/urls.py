from django.urls import path

from . import views


urlpatterns = [
    path('riderequest/',views.new_ride_request, name = 'riderequest'),
    path('riderequest/ridestatus', views.view_status, name ='ridestatus'),
    path('riderequest/shareride',views.share_ride_request,name='shareride'),
    path('riderequest/ridelist',views.chosed_ride, name='ridelist'),
    path('',views.index, name = 'index')
]