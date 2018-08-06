from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ScggjyList, ZakerNews, ZakerNewsTab, BxtZbgg


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # result 接口需要返回的字段，可以指定 "__all__" 展示全部参数
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'url',)


class ScggjySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScggjyList
        fields = ('id', 'title', 'pubData', 'detailLink', 'detailTitle',)


class ZakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZakerNews
        fields = ('id', 'zTitle', 'zSubtitle', 'sSubImageLink', 'zDetailLink', 'zType',)


class ZakerTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZakerNewsTab
        fields = ('id', 'code', 'tabName',)


class ZbggSerializer(serializers.ModelSerializer):
    class Meta:
        model = BxtZbgg
        fields = (
        'id', 'area', 'city', 'ywtype', 'xxtype', 'type', 'ly', 'title', 'pubdata', 'deaddata', 'status', 'itemnum',
        'detailurl')
