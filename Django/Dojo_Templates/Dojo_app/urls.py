from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('process', views.createdojo),
    path('process2', views.createninja),
    path('process3', views.createninja)
]
