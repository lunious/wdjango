from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ScggjyList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'url',)


class ScggjySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScggjyList
        fields = ('id', 'title', 'pubData', 'detailLink', 'detailTitle',)
