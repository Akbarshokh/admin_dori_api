from dataclasses import field
from rest_framework import serializers
from .models import *

class DoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dori
        fields = ['id', 'slug', 'nomi', 'rasmi', 'tarkibi', 'qollanilishi', 'foydalanish_tartibi', ]
        

class YangiliklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ['rasmi', 'title', 'body',]