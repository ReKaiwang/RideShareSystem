from django.shortcuts import render
from ride_request.forms import NewRide,searchRide,ComRide
from ride_request.models import ride_request
from users.models import CustomUser
from django.urls import reverse
from django import forms
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')
def chosed_ride(request):
    if request.method == 'POST':
        oneride = request.POST
        oneride_id = oneride['choice']
        ride = ride_request.objects.get(id=oneride_id)
        ride.PassageNum = ride.PassageNum+int(oneride['sharenum'])
        curr = CustomUser.objects.get(username=request.user.username)
        ride.user.add(curr)
        ride.rider_pair_set.create(username=request.user.username,number=int(oneride['sharenum']))
        ride.save()
        owner = CustomUser.objects.get(username=request.user.username)
        list = owner.ride_request_set.all()
        return render(request, 'ride_request/status_view.html',context={'list':list})
    return render(request, 'ride_request/status_view.html' )
def share_ride_request(request):
    if request.method == 'POST':
        oneride = request.POST
        # if (oneride['begin'] < oneride['end']):
        #     return render(request,"shareride")
        ride_list_all = ride_request.objects.filter(Destination__contains = oneride['Destination'], ride_status = 'O')
        ride_list = []
        for q in ride_list_all:
            if str(q.arriveTime) >= oneride['begin'] and str(q.arriveTime) <= oneride['end']:
                ride_list.append(q)
        return render(request, 'ride_request/sharelist.html', context = {'list':ride_list, 'number':oneride['PassgeN']})
    return render(request, 'ride_request/ride_share_request.html')

def new_ride_request(request):
    form = NewRide
    #curr = CustomUser.objects.get(pk=request.user.username)
    #print(curr)
    if request.method == 'POST':
        form = NewRide(request.POST)
        #print(form)
        if form.is_valid():
            Comform = form.save(commit = False)
            Comform.save()
            curr=CustomUser.objects.get(username=request.user.username)
            Comform.user.add(curr)
           # Comform.save()
            form.save(commit=True)
            Comform.rider_pair_set.create(username=request.user.username,number=Comform.PassageNum,)
            print(Comform.rider_pair_set.all())
            list=curr.ride_request_set.all()
            return render(request,'ride_request/status_view.html',context={"list":list})
        else:
            print("wrong form")
    return render(request, 'ride_request/ride_owner_request.html',context={'form':form})

def view_status(request):
    owner= CustomUser.objects.get(username=request.user.username)
    #oneride = ride_request.objects.get(id=3)
    # oneride = ride_request.objects.filter(Destination__contains = 'Bryan')

    # if request.method == 'POST':
    #     newStatus = request.POST
    #     print(oneride.ride_status)
    #     if oneride.ride_status != 'C':
    #         oneride.arriveTime = newStatus['arriveTime']
    #         oneride.Destination = newStatus['Destination']
    #         oneride.PassageNum = newStatus['PassageNum']
    #         oneride.save()
    #list = ride_request.objects.get(user=owner)
    #print("list is:")
    #print(list)

    list=owner.ride_request_set.all()
    context = {
        'list': list
    }
    if request.method == 'POST':
        newStatus = request.POST
        for i in range(0,list.count()):
            if list[i].ride_status != 'C':
                print(list[i].arriveTime)
                print('YES')
                print(list[i].Destination)
                temp=ride_request.objects.get(id=list[i].id)
                temp.arriveTime = newStatus.getlist('arriveTime')[i]
                temp.Destination =newStatus.getlist('Destination')[i]
                temp.PassageNum = newStatus.getlist('PassageNum')[i]
                print(temp.arriveTime)
                temp.save()
                # print(temp.Destination)
                # print(newStatus.getlist('Destination')[i])

        return render(request, 'ride_request/status_view.html', context={'list':list})
    return render(request, 'ride_request/status_view.html', context=context)

# def edit_status(request):
#     if request.method == 'POST':
#         form = NewRide(request.POST)
#         if form.is_valid():
#             if form.ride_status != 'C':
#                 form.save()
#                 return render(request,'ride_request/status_view.html')
#             else:
#                 print("can't edit!")
#     return render(request, 'ride_request/ride_owner_request.html', context={'form': form})