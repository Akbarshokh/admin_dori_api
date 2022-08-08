from django.urls import path, include
from .views import *

urlpatterns = [
    path('account/', include('rest_framework.urls')),
    
    path('mahsulotlar/', DoriList.as_view()),
    path('mahsulotlar/<slug:slug>', DoriDetail.as_view()),
    # path('mahsulotlar/create', DoriCreate.as_view()),
    # path('mahsulotlar/update/<int:pk>', DoriUpdate.as_view()),
    # path('mahsulotlar/delete/<int:pk>', DoriDelete.as_view()),
    
    path('yangiliklar/', YangiliklarList.as_view()),
    path('yangiliklar/<slug:slug>', YangiliklarDetail.as_view()),
    # path('yangiliklar/create', YangiliklarCreate.as_view()),
    # path('yangiliklar/update/<int:pk>', YangiliklarUpdate.as_view()),
    # path('yangiliklar/delete/<int:pk>', YangiliklarDelete.as_view()),
    path('staff/', StaffList.as_view()),
    path('staff/<int:pk>', StaffDetail.as_view()),
    
    
    path('feedback/', FeedBackList.as_view()),   
    
    path('text/', WebsiteTextList.as_view()),
    path('text/<int:pk>', WebsiteTextDetail.as_view()),
    
    path('comments/text/', CommentsListView.as_view() , name="comment" ),
    path('comments/text/<int:pk>', CommentsDetailView.as_view()),
    
    path('comments/image/', CommentsImageListView.as_view() ),
    path('comments/image/<int:pk>', CommentsImageDetailView.as_view()),
    
     
    path('facebook/get/', FacebookListView.as_view()),
    path('telefon/get/', TelefonListView.as_view()),
    path('email/get/', EmailListView.as_view()),
    path('twitter/get/', TwitterListView.as_view()),
    path('telegram/get/', TelegramListView.as_view()),
    path('instagram/get/', InstagramListView.as_view()),
    
    path('map/get/', MapListView.as_view()),
    path('map/<int:pk>', MapDetailView.as_view()),
]
