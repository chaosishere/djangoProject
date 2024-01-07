from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
#creating room

#rooms = [
    #{'id': 1, 'name':'lets learn python!'},
   # {'id': 2, 'name': 'design me!'},
   # {'id': 3, 'name': 'backend developers'},
#]

def home(request):
    rooms = Room.objects.all() #overwrite the rooms from above to the models and added via admin panel
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)

    return render(request, 'base/room.html',{'room': room})

def createRoom(request):
    form = RoomForm()
    context = {'form':form}

    return render(request, 'base/room_form.html',context)
