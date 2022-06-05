from django.urls import path

from . import views, apis

urlpatterns = [
    path('kisan-portal/', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    
    path('api/', apis.basic, name='basic_data'),

    #path('<int:id>/', views.dummy, name='dummy'),
    #path('<id>/', views.dummy, name='dummy'),
]