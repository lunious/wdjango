from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from wapi.serializers import UserSerializer, ScggjySerializer, ZakerSerializer,ZakerTabSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import ScggjyList, ZakerNews,ZakerNewsTab


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScggjyViewSet(viewsets.ModelViewSet):
    queryset = ScggjyList.objects.all()
    serializer_class = ScggjySerializer


class ZakerViewSet(viewsets.ModelViewSet):
    queryset = ZakerNews.objects.all().order_by('-id')  # 根据id倒序
    serializer_class = ZakerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    # 使用 title 作为另一个筛选条件
    filter_fields = ['zType']
    search_fields = ('zTitle',)
class ZakerTabViewSet(viewsets.ModelViewSet):
    queryset = ZakerNewsTab.objects.all().order_by('id') # 根据id升序
    serializer_class = ZakerTabSerializer

