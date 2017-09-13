# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import User,Textinfo


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Textinfo)
class TextinfoAdmin(admin.ModelAdmin):
    pass