from rest_framework import serializers
from .models import User

from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'email', 'password', 'user_foods')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance, validated_data):
        user = User.objects.get(email=validated_data['email'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user
