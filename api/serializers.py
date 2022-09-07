from rest_framework import serializers
from .models import *


class DoriSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dori
        fields = ['id', 'slug', 'nomi', 'rasmi', 'tarkibi', 'qollanilishi', 'foydalanish_tartibi', ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},            
        }
        

class YangiliklarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Yangiliklar
        fields = ['rasmi', 'title', 'body',]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},            
        }


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'kasbi', 'about', 'telefon', 'email', 
                  'twitter', 'facebook', 'instagram', 'telegram', 'avatar']


class WebsiteTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteText
        fields = ['title', 'body']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['first_name', 'email', 'phone', 'about']


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['name']        
    
        
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailModel
        fields = ['name']


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeModel
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