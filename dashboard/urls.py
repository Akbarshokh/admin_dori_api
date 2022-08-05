from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard_url"),
    
    path('mahsulot/list', mahsulot_list, name='mahsulot_list'),
    path('mahsulot/add/', mahsulot_add, name='mahsulot_add_url'),
    path('mahsulot/<int:pk>/', mahsulot_detail, name='mahsulot_detail'),
    
    path('yangliklar/', yangilik_list, name='yangilik_list'),
    path('yangliklar/add', yangilik_add, name='yangilik_add'),
    path('yangliklar/<int:pk>/', yanglik_detail, name='yangilik_detail'),
    
    path('linklar/', linklar, name='linklar_list'),
    # link add
    path('link/add/', add_link, name='link_add_url'),
    path('email/add/', add_email, name='add_email_url'),
    path('phone/add/', add_phone, name='add_phone_url'),
    path('twitter/add/', add_twitter, name='add_twitter_url'),
    path('facebook/add/', add_facebook, name='add_facebook_url'),
    path('telegram/add/', add_telegram, name='add_telegram_url'),
    path('instagram/add/', add_instagram, name='add_instagram_url'),
    
    path('staff/', staff, name='staff_list'),
    path('staff/<int:pk>', staff_detail, name='staff_detail'),
    path('staff/add', staff_add, name='staff_add'),
    
    path('company/', text, name='company_text'),
    path('company/add', text_add, name='company_text_add'),
    path('company/<int:pk>', text, name='company_text_detail'),
    
]