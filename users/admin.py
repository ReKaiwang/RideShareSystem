# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from  ride_request.models import ride_request

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class RideInline(admin.StackedInline):
    model=ride_request
    extra = 4


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','driver','vehicle_brand','plate_number',
                    'maximum_number_of_passengers','special_vehicle_info',]


admin.site.register(CustomUser, CustomUserAdmin)
