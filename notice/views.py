import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from notice.models import TbCar
from notice.fom import ContactForm

now = datetime.datetime.now()
def index(request):
    if request.method=='get':
        form = ContactForm()  # 实例化类，并传入参数绑定
        art = models.TbCar.objects.order_by("id")[0:10]
    else:
        art = models.TbCar.objects.all()
        form = ContactForm(request.POST)  # 实例化类，并传入参数绑定
        if form.is_valid():  # 判定实例是否合法
            ldict = form.cleaned_data  # 清理实例并产生类字典对象
            if request.POST.get('sel', '') == '查询':
                idunm = ldict['one_name']
                art = models.TbCar.objects.filter(carnum__icontains=idunm)
            if request.POST.get('del', '') == '删除':
                idunm = ldict['one_name']
                TbCar.objects.filter(carnum__icontains=idunm).delete()
                art = models.TbCar.objects.all()
        list1=','.join(request.POST.getlist('vehicle'))
        if 'all_car' in list1:
            art=models.TbCar.objects.all()
        if 'y_car' in list1 and 'm_car' in list1 and 'l_car' in list1:
            art = models.TbCar.objects.order_by("id")
        if 'y_car'not in list1 and 'm_car'not in list1 and 'all_car' not in list1 and 'l_car' in list1:
            art = models.TbCar.objects.filter(carattr='1')
        if 'y_car'not in list1 and 'l_car'not in list1 and 'all_car' not in list1 and 'm_car' in list1:
            art = models.TbCar.objects.filter(carattr__in=[5,6])
        if 'm_car'not in list1 and 'l_car'not in list1 and 'all_car' not in list1 and 'y_car' in list1:
            art = models.TbCar.objects.filter(carattr=2)
        if 'y_car'not in list1 and 'all_car' not in list1 and 'l_car' in list1 and 'm_car' in list1:
            art = models.TbCar.objects.filter(carattr__in=[1,5,6])
        if 'l_car'not in list1 and 'all_car' not in list1 and 'y_car' in list1 and 'm_car' in list1:
            art = models.TbCar.objects.filter(carattr__in=[2,5,6])
        if 'm_car'not in list1 and 'all_car' not in list1 and 'l_car' in list1 and 'y_car' in list1:
            art = models.TbCar.objects.filter(carattr__in=[1,2])
        if request.POST.get('startdate'):
            ftime=request.POST.get('startdate')
            ftime.replace('T','')
            with open('1.txt','w+') as fls:
                fls.write(ftime)
            stime = request.POST.get('stopdate')
            stime.replace('T', '')
            start_datetime =datetime.datetime.strptime(ftime, '%Y-%m-%dT%H:%M')
            end_datetime = datetime.datetime.strptime(stime, '%Y-%m-%dT%H:%M')
            art=models.TbCar.objects.filter(intime__range=(start_datetime, end_datetime))
    return render(request, 'notice/sss.html', {'from':form,'aut': art, 'time': now})

