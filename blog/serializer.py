# coding: utf-8
from rest_framework import serializers
from models import User, Textinfo

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'mail','sex','age','sign')

class TextinfoSerializer(serializers.ModelSerializer):
	# author = UserSerializer()
	class Meta:
		model = Textinfo
		fields = ('title', 'body', 'created_at', 'status', 'author')