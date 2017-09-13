# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  models import User,Textinfo
from serializer import UserSerializer,TextinfoSerializer
from rest_framework import viewsets,filters

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TextinfoViewSet(viewsets.ModelViewSet):
    queryset = Textinfo.objects.all()
    serializer_class = TextinfoSerializer
    # filter_fields = ('author', 'status')