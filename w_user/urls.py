from django.urls import path
from w_user import views

urlpatterns = [
    path('register/', views.register),
    path('register_handle/', views.register_handle),
    path('login/', views.login),
    path('login_handle/', views.login_handle),
    path('info/', views.info),
]
