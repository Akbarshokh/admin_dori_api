from dataclasses import field
from rest_framework import serializers
from .models import *

class DoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dori
        fields = ['id','nomi', 'rasmi', 'tarkibi', 'qollanilishi', 'foydalanish_tartibi', ]
