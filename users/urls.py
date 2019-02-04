# users/urls.py
from django.urls import path
from . import views
from ride_request import urls

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('modify/',views.Modify.as_view(),name='modify'),
]