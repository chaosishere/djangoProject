from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .models import Topic
from .forms import RoomForm
from django.db.models import Q
#creating room

#rooms = [
    #{'id': 1, 'name':'lets learn python!'},
   # {'id': 2, 'name': 'design me!'},
   # {'id': 3, 'name': 'backend developers'},
#]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__contains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    #overwrite the rooms from above to the models and added via admin panel
    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}

    return render(request, 'base/home.html', context)

def room(request, pk):

    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html',{'room': room})

def createRoom(request):
    form = RoomForm()
    context = {'form':form}


    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html',context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) #fetching the previously saved form from databse with (instance)

    #Saving the updated form values with
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room',room.id)

    context = {'form':form}
    return render(request, 'base/room_form.html',context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html',context)

