from unittest.util import _MAX_LENGTH
from urllib import request
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize para teste api"""
    name = serializers.CharField(max_length=10)