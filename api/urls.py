from django.urls import path, include
from .views import *

urlpatterns = [
    path('account/', include('rest_framework.urls')),
    
    path('dori/list/', DoriList.as_view()),
    path('dori/list/<int:pk>/<slug:slug>', DoriDetail.as_view()),
    path('dori/list/create', DoriCreate.as_view()),
    path('dori/list/update/<int:pk>', DoriUpdate.as_view()),
    path('dori/list/delete/<int:pk>', DoriDelete.as_view()),
    
    path('yangiliklar/', YangiliklarList.as_view()),
    path('yangiliklar/create', YangiliklarCreate.as_view()),
    path('yangiliklar/update/<int:pk>', YangiliklarUpdate.as_view()),
    path('yangiliklar/delete/<int:pk>', YangiliklarDelete.as_view()),
    
]

