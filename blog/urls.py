from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^list_all$', 'blog.views.listServer'),
    url(r'^list_proxy$', 'blog.views.listProxy'),
    url(r'^$', 'blog.views.listServer'),
    url(r'^list_group/(.+)/$', 'blog.views.listGroup'),
)
