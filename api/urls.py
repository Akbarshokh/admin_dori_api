from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', include('rest_framework.urls')),
    path('dori/list/', DoriList.as_view()),
    path('dori/list/<int:pk>', DoriDetailView.as_view()),
]

