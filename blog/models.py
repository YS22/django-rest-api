# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	SEX_SET = (
			('M', "男"),
			('F', "女"),
	)
	name = models.CharField(max_length=32)
	mail = models.EmailField()
	sex = models.CharField(choices=SEX_SET,max_length=2)
	age = models.IntegerField(max_length=2)
	sign = models.TextField(max_length=30)

class Textinfo(models.Model):
	STATUS_SET = (
			('draft', "草稿"),
			('public', "公开"),
	)
	title = models.CharField(max_length=128)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.CharField(choices=STATUS_SET, default='public', max_length=8)
	author = models.ForeignKey(User)
	