from django.urls import path, include
from .views import *

urlpatterns = [
    path('account/', include('rest_framework.urls')),
    
    path('mahsulotlar/', DoriList.as_view()),
    path('mahsulotlar/<slug:slug>', DoriDetail.as_view()),
    path('mahsulotlar/create', DoriCreate.as_view()),
    path('mahsulotlar/update/<int:pk>', DoriUpdate.as_view()),
    path('mahsulotlar/delete/<int:pk>', DoriDelete.as_view()),
    
    path('yangiliklar/', YangiliklarList.as_view()),
    path('yangiliklar/<slug:slug>', YangiliklarDetail.as_view()),
    path('yangiliklar/create', YangiliklarCreate.as_view()),
    path('yangiliklar/update/<int:pk>', YangiliklarUpdate.as_view()),
    path('yangiliklar/delete/<int:pk>', YangiliklarDelete.as_view()),
    path('twitter/get/', TwitterListView.as_view())
]

