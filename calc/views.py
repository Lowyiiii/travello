from django.shortcuts import render
from .models import Destination
from rest_framework import viewsets
from .serializers import DestinationSerializers
# Create your views here.


def index(request):

    # des1 = Destination()
    # des1.name = 'California'
    # des1.desc = 'The city that never Sleeps'
    # des1.price = 750
    # des1.image = 'destination_1.jpg'
    # des1.offer = False
    #
    # des2 = Destination()
    # des2.name = 'LA'
    # des2.desc = 'The Peaceful city'
    # des2.price = 800
    # des2.image = 'destination_2.jpg'
    # des2.offer = True
    #
    # des3 = Destination()
    # des3.name = 'California'
    # des3.desc = 'The Operating city'
    # des3.price = 650
    # des3.image = 'destination_3.jpg'
    # des3.offer = False
    #
    # dests = [des1,des2,des3]

    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

class DestinationView(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializers