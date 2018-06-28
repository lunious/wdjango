from django.urls import path
from lunious import views

urlpatterns = [
    path('', views.index),
    path('index_1/', views.index_1),
    path('index_2/', views.index_2),
]
