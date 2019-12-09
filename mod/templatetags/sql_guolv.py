from django import template
import notice
from notice.models import TbGate
from notice.models import TbDict
from notice import models

register = template.Library()
@register.filter('gl_attr')     #通用过滤器，凡是查字典的都可以用这个
def gl_attr(var,arg):
    if var==None:
        st=''
    else:
        try:
            attr=notice.models.TbDict.objects.filter(value=var,item=arg)
            if attr==None:
                st=attr
            else:
                st=attr[0].caption
        except Exception:
            st=''
    return st

@register.filter('gl_none')
def gl_none(var):    #过滤空，现在不用了
    if var == None:
        str1 =' '
    else:
        str1=var
    return str1

@register.filter('congjz')
def congjz(var):     #是否可以充值，
    if var == '':
        st2=''
    else:
        if var > 0:
            st2 ='NO'
        else:
            st2 = 'YES'
    return st2

@register.filter('gate')
def gate(var):   #卡口名称提取
    try:
        if var == None:
            str1 =' '
        else:
            art = notice.models.TbGate.objects.filter(gateid=var)
            str1=art[0].gatename
    except Exception:
        str1=''
    return str1

@register.filter('gl_name')
def gl_name(var):       #人员名称提取
    if var == None:
        str1 =' '
    else:
        try:
            num=notice.models.TbUser.objects.filter(userid=var)
            str1=num[0].username
        except Exception:
            str1=''
    return str1

@register.filter('gl_feemp')
def gl_feemp(var):      #月保费率id
    if var==None:
        str1=11
    else:
        str1=var
    return str1

@register.filter('gl_feetp')
def gl_feetp(var):    #临保费率id
    if var==None:
        str1=1
    else:
        str1=var
    return str1

@register.filter('gl_office')
def gl_office(var):       #office名称提取
    if var == None:
        str1=''
    else:
        try:
            num = notice.models.TbOffice.objects.filter(officeid=var)
            str1=num[0].officename
        except Exception:
            str1=''
    return str1

@register.filter('gl_area')
def gl_area(var):       #停车区域名称提取
    if var == None:
        str1=''
    else:
        try:
            num = notice.models.TbParkarea.objects.filter(areaid=var)
            str1=num[0].areaname
        except Exception:
            str1=''
    return str1

@register.filter('gl_scr')
def gl_scr(var):       #显示屏类型提取
    if var == None:
        str1=''
    else:
        try:
            num = notice.models.TbScreentype.objects.filter(screentype=var)
            str1=num[0].screenname
        except Exception:
            str1=''
    return str1
@register.filter('gl_loudong')
def gl_loudong(var):       #显示屏类型提取
    if var == None:
        str1=''
    else:
        try:
            num = notice.models.Addpath.objects.filter(placeid=var)
            str1=num[0].pathname
        except Exception:
            str1=''
    return str1
