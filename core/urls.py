from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.mainPage,name='mainPage'),
    path('list/',views.listFiles,name='listPage'),
    path('view/<str:pk>/',views.viewPage, name='viewPage'),
    path('delete/<str:pk>/',views.deletePage,name='deletePage'),
    
]
