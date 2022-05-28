from django.urls import path

from . import views

urlpatterns = [
    path('Kisan Portal/', views.index, name='index'),
    path('<int:id>/', views.dummy, name='dummy'),
    path('<id>/', views.dummy, name='dummy'),
]