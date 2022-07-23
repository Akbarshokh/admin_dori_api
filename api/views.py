from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import BasePermission, IsAdminUser

class DoriList(generics.ListCreateAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ['nomi']
    search_fields = ['nomi']
    ordering_fields = ['nomi']
    permission_classes = [IsAdminUser]


class DoriDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    permission_classes = [IsAdminUser]


