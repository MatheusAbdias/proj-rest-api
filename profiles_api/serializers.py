from unittest.util import _MAX_LENGTH
from urllib import request
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serialize para teste api"""
    name = serializers.CharField(max_length=10)

class UserProfileSerizalizer(serializers.ModelSerializer):
    """Serializer o perfil do usuario"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
        """Cria um novo usuario"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Atualizando um usuario"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializador do feed """
    class Meta:
        model = models.ProfileFeedItem
        fields = '__all__'
        extra_kwargs = {'user_profile':{'read_only': True}}
