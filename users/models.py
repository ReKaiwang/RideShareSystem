# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
   # fields=('username','email','vehicle','plate_number','max_num','type')
    DRIVER_STATUS=(
       ('y','yes'),
       ('n','no')
    )

    VEHICLE=(
        ('v','volvo'),
        ('a','audi'),
        ('m','mercedes'),
        ('t','toyota'),
        ('h','honda'),
        ('n','nissan'),
        ('o','other')
    )

    SIZE=(
        ('b','big'),
        ('m','medium'),
        ('l','large')
    )
    username = models.CharField(max_length=150,unique=True,primary_key=False)
    special_vehicle_info=models.CharField(max_length=20,choices=SIZE,default='b')
    driver = models.CharField(choices=DRIVER_STATUS,default='n',max_length=2,
                              help_text='want to become a driver? (ignore the following form if you select no)')
    vehicle_brand=models.CharField(choices=VEHICLE,max_length=10,default='o')
    plate_number = models.CharField(max_length=20,default='NAN')
    maximum_number_of_passengers=models.IntegerField(default='4')

    def __str__(self):
        return self.username