from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from stucampus.account.models import Student
from stucampus.articles.models import Article

class Comment(models.Model):
    content = models.TextField(max_length=200,blank=False)
    create_date =  models.DateField(auto_now_add=True,editable=True)
    likes = models.IntegerField(default=0,blank=True,null=True)
    banned = models.BooleanField(default=False)
    editor = models.ForeignKey(Student,related_name='editor',blank=True)
    article = models.ForeignKey(Article,related_name='article',blank=True)
    create_ip = models.GenericIPAddressField(editable=False,null=True,blank=True)
    reply = models.TextField(max_length=200,blank=True) 
