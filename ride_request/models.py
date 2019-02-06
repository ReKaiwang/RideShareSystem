from django.db import models
from django.urls import reverse
from django.conf import settings
from users.models import CustomUser

# Create your models here.
VEHCILE_TYPE =[
    ('v', 'volvo'),
    ('a', 'audi'),
    ('m', 'mercedes'),
    ('t', 'toyota'),
    ('h', 'honda'),
    ('n', 'nissan'),
    ('o', 'other')
    ]
STATUS_TYPE = [
    ('O', 'Open'),
    ('C', 'Confirmed'),
    ('F', 'Finished')

]
SIZE = (
    ('b', 'big'),
    ('m', 'medium'),
    ('l', 'large')
)
class ride_request(models.Model):
    #user= models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL)
    #owner=models.CharField(max_length=256,blank=True)
    #arriveTime = models.TimeField(blank = False)
    arriveTime = models.CharField(blank=False, max_length=256, help_text="Time Form: xx:xx ")
    Destination = models.CharField(max_length = 256, blank = False)
    PassageNum = models.PositiveSmallIntegerField(blank = False,verbose_name="Passger Number")
    Vehicle_type = models.CharField(max_length = 256, blank = True, choices =VEHCILE_TYPE, help_text="Optional")
    Share = models.BooleanField(blank = False)
    Other_request = models.CharField(max_length = 256, blank =True, help_text="Optional", choices=SIZE)
    ride_status = models.CharField(max_length = 200, blank = True, default = 'O', choices = STATUS_TYPE)
    driver=models.CharField(max_length= 200,blank=True)
    vehicle=models.CharField(max_length= 200,blank=True)
    capacity=models.IntegerField(blank=True,null=True)
    plate=models.CharField(max_length= 200,blank=True)
    info=models.CharField(max_length= 200,blank=True)
    def __str__(self):
        return self.Destination

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

#weddddddddddddddd
class rider_pair(models.Model):
    username=models.CharField(max_length=200,blank=True)
    number=models.IntegerField(blank=True,null=True)
    ride=models.ForeignKey(ride_request,on_delete= models.CASCADE,)
