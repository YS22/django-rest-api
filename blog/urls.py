# coding: utf-8

from rest_framework import routers
from views import UserViewSet, TextinfoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'textinfo', TextinfoViewSet)