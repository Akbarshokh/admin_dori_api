from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


class DoriList(generics.ListAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    
    
    
class DoriDetail(generics.RetrieveAPIView):
    queryset = Dori.objects.all()
    serializer_class = DoriSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
  

class YangiliklarList(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()  
    serializer_class = YangiliklarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class YangiliklarDetail(generics.RetrieveAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
   

class StaffList(generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class StaffDetail(generics.RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class WebsiteTextList(generics.ListAPIView):
    queryset = WebsiteText.objects.all()
    serializer_class = WebsiteTextSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class WebsiteTextDetail(generics.RetrieveAPIView):
    queryset = WebsiteText.objects.all()
    serializer_class = WebsiteTextSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CommentsListView(generics.ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

class CommentsDetailView(generics.RetrieveAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class CommentsImageListView(generics.ListCreateAPIView):
    queryset = CommentImageModel.objects.all()
    serializer_class = CommentsImageSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
       
class CommentsImageDetailView(generics.RetrieveAPIView):
    queryset = CommentImageModel.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class FeedBackList(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
  

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


class YoutubeListView(APIView):
    def get(self, request):
        snippets = YoutubeListView.objects.last()
        serializer = YoutubeSerializer(snippets)
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


class MapDetailView(generics.RetrieveAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]    
    

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
