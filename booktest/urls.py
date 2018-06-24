from django.urls import path

from booktest import views

urlpatterns = [

    path('', views.index),
    path('<int:id>', views.show),
]
