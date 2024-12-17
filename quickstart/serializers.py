from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedSerializer):
    class Meta:
        model = User
        fields = ['url','email','username', 'groups']

class GroupSerializer(serializers.HyperlinkedSerializer):
    class Meta:
        model = Group
        fields = ['url','name']