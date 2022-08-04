from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard_url"),
    
    path('mahsulot/list', mahsulot_list, name='mahsulot_list'),
    path('mahsulot/add/', mahsulot_add, name='mahsulot_add_url'),
    path('mahsulot/<int:pk>/', mahsulot_detail, name='mahsulot_detail'),
    
    path('yangliklar/', yangilik_list, name='yangilik_list'),
    path('yangliklar/add', yangilik_add, name='yangilik_add'),
    path('yangliklar/<int:pk>/', yanglik_detail, name='yanglik_detail'),
    
    path('linklar/', linklar, name='linklar_list'),
    
    path('staff/', staff, name='staff_url'),
]

