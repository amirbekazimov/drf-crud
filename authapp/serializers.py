from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'confirm_password']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
