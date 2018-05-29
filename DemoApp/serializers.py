from rest_framework import serializers
class Hello(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=20)
