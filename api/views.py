import django
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.views import APIView

class DoriList(generics.ListAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]
    
class DoriDetail(generics.RetrieveAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]
  

class DoriCreate(generics.CreateAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]


class DoriUpdate(generics.UpdateAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]
    

class DoriDelete(generics.DestroyAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]


class YangiliklarList(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()  
    serializer_class = YangiliklarSerializer
    permission_classes = [IsAdminUser]

class YangiliklarDetail(generics.RetrieveAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
    permission_classes = [IsAdminUser]

class YangiliklarCreate(generics.CreateAPIView):
    queryset = Yangiliklar.objects.all()  
    serializer_class = YangiliklarSerializer
    permission_classes = [IsAdminUser]


class YangiliklarUpdate(generics.UpdateAPIView):
    queryset = Yangiliklar.objects.all()  
    serializer_class = YangiliklarSerializer
    permission_classes = [IsAdminUser]


class YangiliklarDelete(generics.DestroyAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
    permission_classes = [IsAdminUser]
    

class StaffList(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser]
    
    
class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_class = [IsAdminUser]


class MapList(generics.ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_class = [IsAdminUser]


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_class = [IsAdminUser]


class EmailList(generics.ListAPIView):
    queryset = EmailModel.objects.all()
    serializer_class = EmailSerializer
    permission_class = [IsAdminUser]


class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmailModel.objects.all()
    serializer_class = EmailSerializer
    permission_class = [IsAdminUser]


class TwitterListView(APIView):
    def get(self, request):
        snippets = TwitterModel.objects.last()
        serializer = TwitterSerializer(snippets)
        return Response(serializer.data)