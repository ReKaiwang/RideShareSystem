# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','driver','vehicle_brand','plate_number'
                  ,'maximum_number_of_passengers','special_vehicle_info') #'vehicle', 'plate_number', 'max_num', 'type')


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        #fields = ( 'email','driver','vehicle_brand','plate_number'
        #          ,'maximum_number_of_passengers','special_vehicle_info')
        fields = ['email','driver','vehicle_brand','plate_number'
            ,'maximum_number_of_passengers','special_vehicle_info']