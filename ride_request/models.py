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
class ride_request(models.Model):
    #user= models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    #owner=models.CharField(max_length=256,blank=True)
    #arriveTime = models.TimeField(blank = False)
    arriveTime = models.CharField(blank=False, max_length=256, help_text="Time form: xx:xx p.m/a.m")
    Destination = models.CharField(max_length = 256, blank = False)
    PassageNum = models.PositiveSmallIntegerField(blank = False,verbose_name="Passger Number")
    Vehicle_type = models.CharField(max_length = 256, blank = True, choices =VEHCILE_TYPE)
    Share = models.BooleanField(blank = False)
    Other_request = models.CharField(max_length = 256, blank =True)
    ride_status = models.CharField(max_length = 200, blank = True, default = 'O', choices = STATUS_TYPE)

    def __str__(self):
        return self.Destination

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])
