from rest_framework import serializers
from .models import Destination

class DestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ('id','name','image','desc','price','dest','offer')