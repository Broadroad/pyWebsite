# coding:utf-8
from django.conf.urls import patterns, url

from . import views

from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'weixin2py.views.home', name='home'),
    # url(r'^weixin2py/', include('weixin2py.foo.urls')),
    url(r'^$', views.home),
    url(r'^wuqian/about/(?P<about_type>\w+)/$', views.about,name='wuqian-about'),
    url(r'^wuqian/huodong2/$', views.wuqian_huodong),
    url(r'^wuqian/test/$', views.wuqian_test),
    url(r'^wuqian/iframe/$', views.wuqian_iframe),

    url(r'^wuqian/news/(?P<new_type>\w+)/$', views.news_list),

    url(r'^news/list/(?P<title>\w+)/$', views.get_news_detail),

    url(r'^wuqian/business/(?P<new_type>\w+)/$', views.wuqian_business_list),

    url(r'^wuqian/business/list/(?P<title>\w+)/$', views.get_business_detail),

    url(r'^wuqian/culture/(?P<about_type>\w+)/$', views.wuqian_culture),
    
    url(r'^ability/(?P<about_type>\w+)/$', views.wuqian_ability),

    url(r'^resource/(?P<about_type>\w+)/$', views.wuqian_resource),

    url(r'^wuqian/contact/(?P<about_type>\w+)/$', views.wuqian_contact),
) 

