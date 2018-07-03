from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from wapi import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'scggjyList', views.ScggjyViewSet)
router.register(r'zakerList', views.ZakerViewSet)
# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
