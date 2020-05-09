from rest_framework import serializers

class RegisterUserSerializers(serializers.Serializer):
    username = serializers.CharField(required=True,allow_blank=False,allow_null=False,max_length=200)
    password = serializers.CharField(required=True,allow_blank=False,allow_null=False,max_length=200)
    sex = serializers.CharField(required=True,allow_blank=False,allow_null=False,max_length=200)
