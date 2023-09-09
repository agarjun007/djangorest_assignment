from rest_framework import serializers
from .models import Users, Products


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users(
            username=validated_data['username'],first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ('username', 'password')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'active', 'description', 'price', 'quantity', 'image')
