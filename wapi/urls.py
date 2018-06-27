from django.urls import path
from wapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('wapi/', views.snippet_list),
    path('wapi/<int:pk>/', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
