from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard_url"),
    path('mahsulotlar/', mahsulotlar, name='mahsulotlar_url'),
    path('mahsulot/add/', mahsulot_add, name='mahsulot_add_url'),
    path('mahsulot/<int:pk>/', mahsulot_detail, name='mahsulot_url'),
    path('yangliklar/', yangliklar, name='yangliklar_url'),
    path('yanglik/<int:pk>/', yanglik, name='yanglik_url'),
    path('linklar/', linklar, name='linklar_url'),
    path('staff/', staff, name='staff_url'),
]

