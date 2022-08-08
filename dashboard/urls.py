from django.urls import path, include
from .views import *

urlpatterns = [
    ############### Login and Logout ###############
    path('', login_view, name="login_url"),
    path('logout/', logout_view, name="logout"),
    
    ############### Dashboard ###############
    path('home', dashboard, name="dashboard_url"),
       
    ############### Mahsulotlar ###############
    path('mahsulot/list', mahsulot_list, name='mahsulot_list'),
    path('mahsulot/add/', mahsulot_add, name='mahsulot_add_url'),
    path('mahsulot/<int:pk>/', mahsulot_detail, name='mahsulot_detail'),
    path('mahsulot/update', mahsulot_update, name='mahsulot_edit'),
    path('mahsulot/delete', mahsulot_delete, name='mahsulot_delete'),
    
    ############### Yangiliklar ###############
    path('yangliklar/', yangilik_list, name='yangilik_list'),
    path('yangliklar/add', yangilik_add, name='yangilik_add'),
    path('yangliklar/<int:pk>/', yanglik_detail, name='yangilik_detail'),
    path('yangliklar/update', yangilik_update, name='yangilik_edit'),
    path('yangliklar/delete', yangilik_delete, name='yangilik_delete'),
    
    ############### Linklar ###############
    path('linklar/', linklar, name='linklar_list'),
    path('link/add/', add_link, name='link_add_url'),
    path('email/add/', add_email, name='add_email_url'),
    path('phone/add/', add_phone, name='add_phone_url'),
    path('twitter/add/', add_twitter, name='add_twitter_url'),
    path('facebook/add/', add_facebook, name='add_facebook_url'),
    path('telegram/add/', add_telegram, name='add_telegram_url'),
    path('instagram/add/', add_instagram, name='add_instagram_url'),
    
    ############### Map ###############
    path('map/', map_list, name="map_list"),
    path('map/add/', add_location, name="add_location"),
    path('map/list/', add_map, name="add_map"), 
    # path('map/update', map_update, name="map_update"),
    # path('map/delete', map_delete, name="map_delete"),
    
    ############### Staff ###############
    path('staff/', staff, name='staff_list'),
    path('staff/<int:pk>', staff_detail, name='staff_detail'),
    path('staff/add', staff_add, name='staff_add'),
    path('staff/update', staff_update, name='staff_edit'),
    path('staff/delete', staff_delete, name='staff_delete'),
    
    ############### Website Text ###############
    path('company/', text, name='company_text'),
    path('company/add', text_add, name='company_text_add'),
    path('company/<int:pk>', text, name='company_text_detail'),
    path('company/update', text_update, name='company_text_edit'),
    path('company/delete', text_delete, name='company_text_delete'),
    
    ############### Comments Text ###############
    path('company/comment/text/', text_comment, name='text_comment'),
    path('company/comment/text/<int:pk>', text_comment_detail, name='text_comment_detail'),
    path('company/comment/text/add>', text_comment_add, name='text_comment_add'),    
    path('company/comment/text/update', text_comment_update, name='text_comment_update'),
    path('company/comment/text/delete', text_comment_delete, name='text_comment_delete'),
    
    ############### Comments Images ###############
    path('company/comment/image/', comment_image_list, name='comment_image_list'),
    path('company/comment/image/<int:pk>', comment_image_detail, name='comment_image_detail'),
    path('company/comment/image/add>', comment_image_add, name='comment_image_add'),    
    path('company/comment/image/update', comment_image_update, name='comment_image_update'),
    path('company/comment/image/delete', comment_image_delete, name='comment_image_delete'),
    
    ############### Feedback ###############
    path('feedback/list', feedback_list, name="feedback_list"),
    path('feedback/<int:pk>', feedback_detail , name="feedback_detail"),  
]