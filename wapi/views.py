from wapi.serializers import UserSerializer, ScggjySerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import ScggjyList


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScggjyViewSet(viewsets.ModelViewSet):
    queryset = ScggjyList.objects.all()
    serializer_class = ScggjySerializer
