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
from .gsheets import *

class DoriList(generics.ListAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]
    
    
class DoriDetail(generics.RetrieveAPIView):
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
   

class StaffList(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAdminUser]
    
    
class StaffDetail(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_class = [IsAdminUser]


class WebsiteTextList(generics.ListAPIView):
    queryset = WebsiteText.objects.all()
    serializer_class = WebsiteTextSerializer
    permission_classes = [IsAdminUser]


class WebsiteTextDetail(generics.RetrieveAPIView):
    queryset = WebsiteText.objects.all()
    serializer_class = WebsiteTextSerializer
    permission_classes = [IsAdminUser]


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class FacebookListView(APIView):
    def get(self, request):
        snippets = FacebookModel.objects.last()
        serializer = FacebookSerializer(snippets)
        return Response(serializer.data)


class TelefonListView(APIView):
    def get(self, request):
        snippets = TelefonModel.objects.last()
        serializer = TelefonSerializer(snippets)
        return Response(serializer.data)


class EmailListView(APIView):
    def get(self, request):
        snippets = EmailModel.objects.last()
        serializer = EmailSerializer(snippets)
        return Response(serializer.data)


class MapListView(APIView):
    def get(self, request):
        snippets = Map.objects.last()
        serializer = MapSerializer(snippets)
        return Response(serializer.data)


class TwitterListView(APIView):
    def get(self, request):
        snippets = TwitterModel.objects.last()
        serializer = TwitterSerializer(snippets)
        return Response(serializer.data)


class TelegramListView(APIView):
    def get(self, request):
        snippets = TelegramModel.objects.last()
        serializer = TelegramSerializer(snippets)
        return Response(serializer.data)
    
    
class InstagramListView(APIView):
    def get(self, request):
        snippets = InstagramModel.objects.last()
        serializer = InstagramSerializer(snippets)
        return Response(serializer.data)
