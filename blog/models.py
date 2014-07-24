# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class Person(models.Model):
    name = models.CharField('作者姓名', max_length=10)
    age = models.IntegerField('作者年龄')

class Book(models.Model):
    person =models.ManyToManyField(Person, related_name='person_book')
    title =models.CharField('书籍名称', max_length=10)
    pubtime =models.DateField('出版时间')

#class RealServer(models.Model):
#    ServerName = models.CharField(max_length = 150)
#    WlanIp = models.IPAddressField()
#    LanIp = models.IPAddressField()
#    ManagerIp = models.IPAddressField()
#    Usefor = models.CharField(max_length = 150)
#    Notification = models.BooleanField()
#
#class LvsServer(models.Model):
#    ServerId = models.ForeignKey(RealServer, unique=True)
#    ProxyGroupId = models.IntegerField(max_length = 100)
#    DomainNameId = models.IntegerField(max_length = 100)
#    Status = models.CharField(max_length = 150)
#
#class LvsGroup(models.Model):
#    LvsGroupId = models.IntegerField(max_length = 100)
#    LvsGroupName = models.CharField(max_length = 150)
#    Servers = models.ManyToMany()
#
#class ProxyServer(models.Model):
#    ProxyServerId = models.IntegerField(max_length = 100)
#    ProxyGroupId = models.IntegerField(max_length = 100)
#    ServerId = models.ForeignKey(RealServer, unique=True)
#
#class ProxyGroup(models.Model):
#    GroupId = models.IntegerField(max_length = 100)
#    ProxyServerId = models.ForeignKey(ProxyServer, unique=True)
#
#class DomainList(models.Model):
#    DomainName = models.CharField(max_length = 150)
#    ProxyGroupId = models.ForeignKey(ProxyGroup, unique=True)
#    LvsGroupId = models.ForeignKey(LvsGroup, unique=True)
#    AppServerGroupId = models.ForeignKey(AppServerGroup, unique=True)

#admin.site.register(BlogsPost)
#admin.site.register(RealServer)
#admin.site.register(ProxyServer)
admin.site.register(Person)
admin.site.register(Book)
