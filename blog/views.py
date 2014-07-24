from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import *

# Create your views here.

def archive(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))

def listServer(request):
    servers = RealServer.objects.all()
    t = loader.get_template("lvsmember.html")
    c = Context({'servers': servers})
    return HttpResponse(t.render(c))

def index(request):
    servers = RealServer.objects.all()
    t = loader.get_template("lvsmember.html")
    c = Context({'servers': servers})
    return HttpResponse(t.render(c))

def listProxy(request):
    ProxyInfos = []
    proxy_servers = ProxyServer.objects.all()
    for proxy_server in proxy_servers:
        ProxyInfos.append(proxy_server)
    t = loader.get_template("proxymember.html")
    c = Context({'proxy_servers': ProxyInfos })
    return HttpResponse(t.render(c))

def listGroup(request, domain):
    ProxyInfos = []
    proxy_servers = ProxyServer.objects.all()
    for proxy_server in proxy_servers:
        ProxyInfos.append(proxy_server)
    t = loader.get_template("proxymember.html")
    c = Context({'proxy_servers': ProxyInfos })
    return HttpResponse(t.render(c))

