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


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'kasbi', 'about', 'email', 
                  'twitter', 'facebook', 'instagram', 'linkedin', 'avatar']


class WebsiteTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteText
        fields = ['title', 'body', 'rasmi']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['first_name', 'email', 'phone', 'about']


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['map']        
    
        
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailModel
        fields = ['name']


class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterModel
        fields = ['name']
 
        
class TelefonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelefonModel
        fields = ['name']


class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookModel
        fields = ['name']
        

class TelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterModel
        fields = ['name']
        

class InstagramSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramModel
        fields = ['name']
        

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['title', 'body']


class CommentsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImageModel
        fields = ['image']