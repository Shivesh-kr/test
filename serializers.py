from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Crime, Station


class CriemesSerializer(serializers.ModelSerializer):
    class Meta:
         model = Crime
         fields = ['reported_by', 'reported_on', 'image', 'station', 'description', 'lat', 'lon', 'type', 'reviewd']


class StationSerializer(serializers.ModelSerializer):
    class Meta:
         model = Station
         fields = ['pk', 'title', 'location', 'pincode', 'incharge', 'lat', 'lon', 'contact']