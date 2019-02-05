from django.db import models
from django import forms
from ride_request.models import ride_request

class NewRide(forms.ModelForm):
    class Meta:
        model = ride_request
        exclude = ['user','ride_status']
        #fields = '__all__'

class ComRide(forms.ModelForm):
    class Meta:
        model = ride_request
        fields = '__all__'

class searchRide(forms.ModelForm):
    class Meta:
        model = ride_request
        fields = ['arriveTime','Destination','PassageNum','Vehicle_type','Other_request']
        # field_classes = {
        #     'arriveTime': forms.DurationField
        # }