from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from . import serializers
from url_filter.integrations.drf import DjangoFilterBackend
from .models import Crime, Station
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CrimeViewSet(viewsets.ModelViewSet):
     queryset = Crime.objects.all().order_by('-created_on')
     serializer_class = serializers.CriemesSerializer
     filter_backends = [DjangoFilterBackend]
     filter_fields = '__all__'


class StationViewSet(viewsets.ModelViewSet):
     queryset = Station.objects.all().order_by('-created_on')
     serializer_class = serializers.StationSerializer
     filter_backends = [DjangoFilterBackend]
     filter_fields = '__all__' 