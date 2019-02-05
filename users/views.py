# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from users.models import CustomUser
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Modify(request):
    #form = CustomUserChangeForm
    list = CustomUser.objects.get(username=request.user.username)
    # form.fields['email']=temp.email
    # form.fields['driver']=temp.driver
    # form.fields['vehicle_brand']=temp.vehicle_brand
    # form.fields['plate_number']= temp.plate_number
    # form.fields['maximum_number_of_passengers']=temp.maximum_number_of_passengers
    # form.fields['special_vehicle_info']=    temp.special_vehicle_info
    #curr = CustomUser.objects.get(pk=form.user.username)
    #print(curr)
    context={
        'usr':list
    }
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        #print(form)
        #['email','driver','vehicle_brand','plate_number'
        #    ,'maximum_number_of_passengers','special_vehicle_info']
        if form.is_valid():
            newStatus = request.POST
            temp = CustomUser.objects.get(username=request.user.username)
            temp.email=newStatus['email']
            temp.driver=newStatus['driver']
            temp.vehicle_brand = newStatus['vehicle_brand']
            temp.plate_number = newStatus['plate_number']
            temp.maximum_number_of_passengers = newStatus['maximum_number_of_passengers']
            temp.special_vehicle_info = newStatus['special_vehicle_info']
            # subject='Confirm your ride'
            # message='Hi '+request.user.username+' your ride has been claimed.'
            # receiver=['zhzheng27@gmail.com']
            # send_mail(subject, message, settings.EMAIL_HOST_USER,
            #           receiver,)

            temp.save()

            return render(request,'modify.html',context={"form": form})
        else:
            print("wrong form")
    return render(request, 'modify.html',context=context)




