from django.shortcuts import render

from .models import Destination

# Create your views here.

def index(request):
    
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.descp = "commercial capital of India"
    dest1.price = 700

    dest2 = Destination()
    dest2.name = "Kerala"
    dest2.descp = "Gods own country"
    dest2.price = 1200

    dest3 = Destination()
    dest3.name = "Sikkim"
    dest3.descp = "natural beauty and Buddhism"
    dest3.price = 950

    return render(request, 'index.html', {'dest1' : dest1, 'dest2' : dest2, 'dest3' : dest3 })
