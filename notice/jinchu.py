import datetime
from django.shortcuts import render
from django.http import HttpResponse
import notice
from notice.models import TbCarpass
from notice.fom import ContactForm
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.http import JsonResponse
#from django.core import serializers    #下面启用上面也启用
import os
now = datetime.datetime.now()
def jinchux(request):
    if request.method=='get':
        form = ContactForm()  # 实例化类，并传入参数绑定
        art = notice.models.TbCarpass.objects.order_by("-autoid")[0:500]
    else:
        art = notice.models.TbCarpass.objects.order_by("-autoid")[0:500]
        form = ContactForm(request.POST)  # 实例化类，并传入参数绑定
        if form.is_valid():  # 判定实例是否合法
            ldict = form.cleaned_data  # 清理实例并产生类字典对象
            if request.POST.get('sel', '') == '查询':
                idunm = ldict['one_name']
                art = notice.models.TbCarpass.objects.filter(carnum__icontains=idunm)
            if request.POST.get('del', '') == '删除':
                idunm = ldict['one_name']
                #TbCarpass.objects.filter(carnum__icontains=idunm).delete()
                art = notice.models.TbCarpass.objects.all()
        list1=','.join(request.POST.getlist('vehicle'))
        if 'all_car' in list1:
            art=notice.models.TbCarpass.objects.order_by("-autoid")[0:1000]
        if 'y_car' in list1 and 'm_car' in list1 and 'l_car' in list1:
            art = notice.models.TbCarpass.objects.order_by("-autoid")[0:1000]
        if 'y_car'not in list1 and 'm_car'not in list1 and 'all_car' not in list1 and 'l_car' in list1:
            art = notice.models.TbCarpass.objects.filter(carattr='1').order_by("-autoid")[0:300]
        if 'y_car'not in list1 and 'l_car'not in list1 and 'all_car' not in list1 and 'm_car' in list1:
            art = notice.models.TbCarpass.objects.filter(carattr__in=[5,6]).order_by("-autoid")[0:300]
        if 'm_car'not in list1 and 'l_car'not in list1 and 'all_car' not in list1 and 'y_car' in list1:
            art = notice.models.TbCarpass.objects.filter(carattr=2).order_by("-autoid")[0:300]
        if 'y_car'not in list1 and 'all_car' not in list1 and 'l_car' in list1 and 'm_car' in list1:
            art =notice.models.TbCarpass.objects.filter(carattr__in=[1,5,6]).order_by("-autoid")[0:300]
        if 'l_car'not in list1 and 'all_car' not in list1 and 'y_car' in list1 and 'm_car' in list1:
            art = notice.models.TbCarpass.objects.filter(carattr__in=[2,5,6]).order_by("-autoid")[0:300]
        if 'm_car'not in list1 and 'all_car' not in list1 and 'l_car' in list1 and 'y_car' in list1:
            art = notice.models.TbCarpass.objects.filter(carattr__in=[1,2]).order_by("-autoid")[0:300]
        if request.POST.get('startdate'):
            ftime=request.POST.get('startdate')
            stime = request.POST.get('stopdate')
            start_datetime =datetime.datetime.strptime(ftime, '%Y-%m-%dT%H:%M')
            end_datetime = datetime.datetime.strptime(stime, '%Y-%m-%dT%H:%M')
            art=notice.models.TbCarpass.objects.filter(time__range=(start_datetime, end_datetime))
    paginator = Paginator(art, 30)
    page=request.GET.get('page')
    try:
        cust=paginator.page(page)
    except PageNotAnInteger:
        cust=paginator.page(1)
    except EmptyPage:
        cust=paginator.page(paginator.num_pages)
    return render(request, 'notice/jinchu.html', {'from':form,'aut': cust, 'time': now,'cust':cust})

def jxja(request):
    if request.method == 'POST':
        if request.is_ajax():
            aa=request.POST.get('name')
            if aa != '':
                aut = notice.models.TbCarpass.objects.filter(autoid=aa).order_by("-autoid")[0:1]
                #data = serializers.serialize("json", aut)    #这条语句可以直接将数据库对象转化为json格式发送，如果发送的是字典就不用了
                #for x in aut:
                dat=aut[0].fullpic
                name1=str(aut[0].autoid)+'.png'
                r1='C:\\Users\\qjb-pc\\HelloWorld\\notice\static\\images\\'    #这里的路径不许用双斜杠
                di1=os.path.join(r1,name1)
                with open(di1,'wb+' )as f:
                    f.write(dat)
                    f.close()                        #上面的一段是将二进制图片流保存到本地，然后让他们按id号命名
                data1={
                    'carnum':aut[0].carnum,
                    'autoid':aut[0].autoid,
                    'pna':name1,
                    'intime':aut[0].intime,
                    'outime':aut[0].outime,
                    'time':aut[0].time,
                    'carnumread':aut[0].carnumread,       #组织json数据
                }
            else:
                data1={'erro':'数据加载失败'}
    return JsonResponse(data1, safe=False)       #发送json数据，safe要设为false
