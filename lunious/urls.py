from django.urls import path
from lunious import views

urlpatterns = [
    path('', views.index_1),
]