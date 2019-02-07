from django.shortcuts import render
from ride_request.forms import NewRide,searchRide,ComRide
from ride_request.models import ride_request
from users.models import CustomUser
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def find_ride(request):
    list = ride_request.objects.filter(ride_status__contains = 'O', Vehicle_type = request.user.vehicle_brand)
    ride_list = []
    # print(list)
    for q in list:
        # print(q.PassageNum)
        # print(len(q.Other_request))
        # print(len(request.user.special_vehicle_info))
        if len(q.Vehicle_type) == 0 or q.Vehicle_type == request.user.vehicle_brand:
            if q.PassageNum <= request.user.maximum_number_of_passengers:
             if len(q.rider_pair_set.filter(username=request.user.username)) == 0:
                if len(q.Other_request)==0 :
                    ride_list.append(q)
                elif q.Other_request == request.user.special_vehicle_info:
                    ride_list.append(q)

    number = len(ride_list)
    #print(ride_list)
    context = {
        'list': ride_list,
        'number':number
    }
    if request.method == 'POST':
        oneride_id = request.POST['choice']
        ride = ride_request.objects.get(id=oneride_id)
        ride.ride_status = 'C'
        curr = CustomUser.objects.get(username=request.user.username)
        ride.user.add(curr)
        ride.save()
        owner = CustomUser.objects.get(username=request.user.username)
        list = owner.ride_request_set.filter(ride_status__contains = 'C')
        ride.driver=request.user.username
        ride.vehicle=request.user.vehicle_brand
        ride.capacity=request.user.maximum_number_of_passengers
        ride.plate=request.user.plate_number
        ride.info=request.user.special_vehicle_info
        ride.save()
        subject = 'Confirm your ride'
        # need exclude the driver
        owner=ride.user.all()
        #receiver=[]
        for i in owner:
            receiver=[]
            receiver.append(i.email)
            message = 'Hi ' + i.username + ' your ride to ' + ride.Destination+' at '+ ride.arriveTime + ' has been claimed.'
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      receiver, )


        return render(request, 'driver/status_view.html',context={'list':list} )
    return render(request, 'driver/ride_driver.html',context=context )

def ride_view(request):
    owner = CustomUser.objects.get(username=request.user.username)
    list = owner.ride_request_set.filter(ride_status__contains = 'C')
    number = len(list)
    context = {
        'list': list,
        'number': number
    }
    if request.method == 'POST':
        oneride_id = request.POST['finish']
        ride = ride_request.objects.get(id=oneride_id)
        ride.ride_status = 'F'
        ride.save()
        owner = CustomUser.objects.get(username=request.user.username)
        list = owner.ride_request_set.filter(ride_status__contains = 'C')
        number = len(list)
        #print('YES')
        print(ride.rider_pair_set)
        # userlist=[]
        # for i in list:
        #     userlist.append(i.ride_request_set.all())
        #     print(i.ride_request_set.all()[0].user)
        return render(request, 'driver/status_view.html', context={'list': list, 'number':number})
    return render(request, 'driver/status_view.html', context=context)