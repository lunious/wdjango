from django.urls import path
from lunious import views

urlpatterns = [
    path('', views.index),
    path('index1/', views.index1),
    path('index2/', views.index2),
]
