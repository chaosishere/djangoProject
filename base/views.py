from django.shortcuts import render
from django.http import HttpResponse

#creating room

rooms = [
    {'id': 1, 'name':'lets learn python!'},
    {'id': 2, 'name': 'design me!'},
    {'id': 3, 'name': 'backend developers'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    return render(request, 'base/room.html',{'room': room})

