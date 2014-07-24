from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class RealServer(models.Model):
    ServerName = models.CharField(max_length = 150)
    WlanIp = models.IPAddressField()
    LanIp = models.IPAddressField()
    ManagerIp = models.IPAddressField()
    Usefor = models.CharField(max_length = 150)
    Notification = models.BooleanField()

class LvsServer(models.Model):
    ServerId = models.ForeignKey(RealServer, unique=True)
    ProxyGroupId = models.IntegerField(max_length = 100)
    DomainNameId = models.IntegerField(max_length = 100)
    Status = models.CharField(max_length = 150)

class ProxyServer(models.Model):
    ProxyServerId = models.IntegerField(max_length = 100)
    ProxyGroupId = models.IntegerField(max_length = 100)
    ServerId = models.ForeignKey(RealServer, unique=True)

class ProxyGroup(models.Model):
    GroupId = models.IntegerField(max_length = 100)
    ProxyServerId = models.ForeignKey(ProxyServer, unique=True)

admin.site.register(BlogsPost)
admin.site.register(RealServer)
admin.site.register(ProxyServer)
