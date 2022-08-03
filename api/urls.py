from django.urls import path, include
from .views import *

urlpatterns = [
    path('account/', include('rest_framework.urls')),
]
