# coding:utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template import Context
from wuqian.models.home_page import HomePage
from wuqian.models.news import News
from wuqian.models.about_wuqian import AboutWuqian
from wuqian.models.wuqian_business import WuqianBusiness
from wuqian.models.company_culture import CompanyCulture
from wuqian.models.human_resources import HumanResource
from wuqian.models.social_ability import SocialAbility
from wuqian.models.contact_us import ContactUs
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    home_list = HomePage.objects.all()
    if len(home_list) == 0:
        raise Exception(u"首页还没有配置呢！")
    for key in home_list:
        context = RequestContext(request, {
            'home':key,
        })
    return render(request, 'wuqian/wuqian-index.html',context)

def get_news_detail(request,title):
    new = News.objects.get(title=title)
    context = RequestContext(request, {
        'new':new,              
        new.news_type: 'her',
    })  
    return render(request, 'wuqian/wuqian-news-detail.html',context)

def news_list(request, new_type):
    news_list = News.objects.filter(news_type = new_type)
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    p = Paginator(news_list, 5) 
    try:
        page = p.page(page)
    except:
        page = None
    context = RequestContext(request, {
        'news': page,
        new_type: 'her',
    })
    return render(request, 'wuqian/wuqian-news-list.html',context)

def wuqian_business_list(request, new_type):
    news_list = WuqianBusiness.objects.filter(news_type = new_type)
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    p = Paginator(news_list, 12) 
    try:
        page = p.page(page)
    except:
        page = None
    context = RequestContext(request, {
        'news': page,
        new_type: 'her',
    })
    return render(request, 'wuqian/wuqian-bus-list.html',context)

def get_business_detail(request,title):
    new = WuqianBusiness.objects.get(title=title)
    context = RequestContext(request, {
        'new':new,              
        new.news_type: 'her',
    })  
    return render(request, 'wuqian/wuqian-bus-detail.html',context)

def about(request, about_type):
    about_list = AboutWuqian.objects.all()
    if len(about_list) == 0:
        raise Exception(u"关于页面还没有配置呢！")
    about_wuqian = None
    for about in about_list:
        about_wuqian = about
    about_wuqian_map = {
        'wuqiangaishu': about_wuqian.wuqiangaishu,
        'wuqianzhanlve': about_wuqian.wuqianzhanlve,
        'hexinyoushi': about_wuqian.hexinyoushi,
        'fazhanlicheng': about_wuqian.fazhanlicheng,
    }
    context = RequestContext(request, {
        'about':about_wuqian_map[about_type],
        about_type: 'her',
    })  
    return render(request, 'wuqian/wuqian-about.html',context)

def wuqian_culture(request, about_type):
    about_list = CompanyCulture.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_wuqian = None
    for about in about_list:
        about_wuqian = about
    about_wuqian_map = {
        'guanlizhidao': about_wuqian.guanlizhidao,
        'qiyezongzhi': about_wuqian.qiyezongzhi,
        'qiyejinshen': about_wuqian.qiyejinshen,
        'qiyezuoyong': about_wuqian.qiyezuoyong,
    }
    context = RequestContext(request, {
        'about':about_wuqian_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-culture.html',context)

def wuqian_ability(request, about_type):
    about_list = SocialAbility.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_wuqian = None
    for about in about_list:
        about_wuqian = about
    about_wuqian_map = {
        'gongyilinian': about_wuqian.gongyilinian,
        'cishanjuanzhu': about_wuqian.cishanjuanzhu,
        'shehuizanyu': about_wuqian.shehuizanyu,
    }
    context = RequestContext(request, {
        'about':about_wuqian_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-ability.html',context)

def wuqian_resource(request, about_type):
    about_list = HumanResource.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_wuqian = None
    for about in about_list:
        about_wuqian = about
    about_wuqian_map = {
        'renlilinian': about_wuqian.renlilinian,
        'shehuizhaopin': about_wuqian.shehuizhaopin,
        'xiaoyuanzhaopin': about_wuqian.xiaoyuanzhaopin,
    }
    context = RequestContext(request, {
        'about':about_wuqian_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-resource.html',context)

def wuqian_contact(request, about_type):
    about_list = ContactUs.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置呢！")
    about_wuqian = None
    for about in about_list:
        about_wuqian = about
    about_wuqian_map = {
        'wuqianzongbu': about_wuqian.wuqianzongbu,
        'xiashugongsi': about_wuqian.xiashugongsi,
    }
    context = RequestContext(request, {
        'about':about_wuqian_map[about_type],
        about_type: 'her',
    }) 
    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-contact.html',context)

def wuqian_huodong(request):
    about_list = ContactUs.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置")

    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-huodong.html')


def wuqian_test(request):
    about_list = ContactUs.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置")

    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-test.html')


def wuqian_iframe(request):
    about_list = ContactUs.objects.all()
    if len(about_list) == 0:
        raise Exception(u"页面还没有配置")

    #return HttpResponse(template.render(context))
    return render(request, 'wuqian/wuqian-iframe.html')
