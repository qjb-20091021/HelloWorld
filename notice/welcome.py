import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context
import json
import notice
from . import models
from notice import models
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
import notice.fenye
import os
from django.core import serializers
from . import rpc_cilent

now = datetime.datetime.now()
def indexs(request):      #主页信息页视图
    feesu=notice.models.TbCarpay.objects.all().count()
    jinsu=notice.models.TbCarpass.objects.all().count()
    carsu=notice.models.TbCar.objects.all().count()
    usesu=notice.models.TbUser.objects.all().count()
    parkdz = notice.models.TbSysref.objects.filter(refname='parkaddress')
    parkname = notice.models.TbSysref.objects.filter(refname='parkname')
    s=datetime.date.today()
    yearfee=notice.models.TjPkyearpay.objects.filter(year=s.year,officetype=-1)
    monthfee = notice.models.TjPkmonthpay.objects.filter(year=s.year,month=s.month, officetype=-1)
    dayfee = notice.models.TjPkdaypay.objects.filter(date=s, officetype=-1)
    dayjinsu = notice.models.TjPkdaypass.objects.filter(date=s,gatetype=-1)
    monthtongji = notice.models.TjPkmonthpay.objects.filter(year=s.year,  officetype=-1)
    yeartongji = notice.models.TjPkyearpay.objects.filter(officetype=-1)
    monlist=[]
    yearlist=[]
    yeardatelist=[]
    yeartdatelist=[]
    yearmdatelist=[]
    datelist=[]
    tdatelist=[]
    mdatelist=[]
    yearlist.append('年份')
    yeardatelist.append('总收费')
    yeartdatelist.append('总收临停缴费')
    yearmdatelist.append('总收月保缴费')
    monlist.append('月份')
    datelist.append('总收费')
    tdatelist.append('临停缴费')
    mdatelist.append('月保缴费')
    for mon in monthtongji:
        monlist.append(str(mon.month)+'月')
        datelist.append(str(mon.paid))
        tdatelist.append( str(mon.t_paid))
        mdatelist.append(str(mon.m_paid))
    for yea in yeartongji:
        yearlist.append(str(yea.year)+'年')
        yeardatelist.append(str(yea.paid))
        yeartdatelist.append(str(yea.t_paid))
        yearmdatelist.append(str(yea.m_paid))

    c = {'feesu':feesu,
                 'jinsu':jinsu,
                 'carsu':carsu,
                 'yearfee':yearfee,
                 'monthfee':monthfee,
                'dayfee':dayfee,
                'usesu':usesu,
                'parkname':parkname,
                'parkdz':parkdz,
                'date':s,
                'dayjinsu':dayjinsu,
                'now':now,
                'monlist':json.dumps(monlist),
                'datelist':json.dumps(datelist),
                'tdatelist': json.dumps(tdatelist),
                'mdatelist': json.dumps(mdatelist),
                 'yearlist': json.dumps(yearlist),
                 'yeardatelist': json.dumps(yeardatelist),
                 'yeartdatelist': json.dumps(yeartdatelist),
                 'yearmdatelist': json.dumps(yearmdatelist),
    }
    return render(request, 'notice/welcome.html', c)

def shouye(request):                  #主页视图
    return render(request, 'notice/shouye.html')


def member_yemian(request):  # 用户空页面
    return render(request, 'notice/member-list1.html')


def member_list(request):  # 用户页面数据
    use = notice.models.TbUser.objects.order_by("-userid")
    cust1 = notice.fenye.split_page(use, request, per_page=15)
    use_list = []
    for us in use:
        u_dict = {}
        u_dict['userid'] = us.userid
        u_dict['username'] = us.username
        u_dict['sex'] = us.sex
        u_dict['opname'] = us.sex
        u_dict['address'] = us.address
        u_dict['mobile'] = us.mobile
        u_dict['regdate'] = us.regdate
        u_dict['placeid'] = us.placeid
        u_dict['usertype'] = us.usertype
        use_list.append(u_dict)
    num = notice.models.TbUser.objects.all().count()
    c = {"code": 0, "msg": "", "count": num, "data": use_list}
    return JsonResponse(c, safe=False)

def fee_list(request):                 #月保费表视图
    use = notice.models.TbCarpay.objects.filter(carattr=2).order_by("-time")
    cust2 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust2}
    return render(request, 'notice/order-list.html', c)

def linfee_list(request):     #临保费表视图
    use = notice.models.TbCarpay.objects.filter(carattr=1).order_by("-time")
    cust3 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust3}
    return render(request, 'notice/orderlin-list.html', c)

def banfee_list(request):    #当班收费视图
    use = notice.models.TbParkduty.objects.all().order_by("-ontime")
    cust5 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust5}
    return render(request, 'notice/banfee-list.html', c)

def yue_list(request):    #月保车视图
    use = notice.models.TbCar.objects.filter(carattr=2).order_by("-regdate")
    cust4 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust4}
    return render(request, 'notice/yuecar-list.html', c)

def lin_list(request):    #临保车视图
    use = notice.models.TbCar.objects.filter(carattr=1).order_by("-regdate")
    cust5 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust5}
    return render(request, 'notice/lincar-list.html', c)

def mian_list(request):    #免费车视图
    use = notice.models.TbCar.objects.filter(carattr__in=[5,6]).order_by("-regdate")
    cust6 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust6}
    return render(request, 'notice/miancar-list.html', c)
def admin_list(request):    #操作员视图
    use = notice.models.TbOperator.objects.all()
    cust7 = notice.fenye.split_page(use, request, per_page=15)
    c = {'use': cust7}
    return render(request, 'notice/admin-list.html', c)

def jilu_list(request):    #历史记录视图
    use = notice.models.TbCarpass.objects.order_by("-autoid")
    cust=notice.fenye.split_page(use,request,per_page=15)
    c = {'use': cust}
    return render(request, 'notice/jilu-list.html', c)
def shijilu_list(request):    #实时记录视图
    use = notice.models.TbCarpass.objects.order_by("-autoid")[0:100]
    c = {'use': use}
    return render(request, 'notice/shijilu-list.html', c)
def shebei_list(request):    #设备记录视图
    cam = notice.models.TbCamera.objects.all()
    scr = notice.models.TbScreen.objects.all()
    spk = notice.models.TbSpk.objects.all()
    sobe = notice.models.TbStrobe.objects.all()
    c = {'cam': cam,'scr':scr,'spk':spk,'sobe':sobe}
    return render(request, 'notice/shebei-list.html', c)

def kakou_list(request):    #卡口视图
    use = notice.models.TbGate.objects.all()
    c = {'use': use}
    return render(request, 'notice/kakou-list.html', c)

def quyu_list(request):    #区域视图
    use = notice.models.TbParkarea.objects.all()
    c = {'use': use}
    return render(request, 'notice/quyu-list.html', c)

def feebz_list(request):    #区域视图
    use = notice.models.TbParkprice.objects.all()
    c = {'use': use}
    return render(request, 'notice/feebz-list.html', c)
def gangting_list(request):    #工作点视图
    use = notice.models.TbOffice.objects.all()
    c = {'use': use}
    return render(request, 'notice/gangting-list.html', c)
def adminlogo_list(request):    #日志视图
    use = notice.models.TbLog.objects.order_by("-autoid")[0:100]
    c = {'use': use}
    return render(request, 'notice/adminlogo-list.html', c)
def xianchangsys_list(request):    #系统视图
    use = notice.models.TbSysref.objects.all()
    c = {'use': use}
    return render(request, 'notice/xianchangsys-list.html', c)
data_user ={}
def jxja_chaxunuser(request):   #接受查询人员请求
    global data_user
    if request.method == 'POST':
        if request.is_ajax():
            if request.POST.get('username'):
                aa=request.POST.get('username') #按姓名
                print(aa)
                user =notice.models.TbUser.objects.filter(username=aa).values()
                cust6 = notice.fenye.split_page(user, request, per_page=15)
                data_user = {'use':cust6}
                data = {'use':''}   #伪装回调数据其实成功后不需要
            if request.POST.get('start'):  #按时间查询
                ftime = request.POST.get('start')
                stime = request.POST.get('end')
                if stime == '':
                    stime = datetime.date.today().__format__('%Y-%m-%d')
                if ftime == '':
                    ftime ='2000-1-1'
                start_date = datetime.datetime.strptime(ftime, '%Y-%m-%d')
                end_date = datetime.datetime.strptime(stime, '%Y-%m-%d')
                art = notice.models.TbUser.objects.filter(regdate__range=(start_date, end_date))
                cust6 = notice.fenye.split_page(art, request, per_page=15)
                data_user = {'use': cust6}
                data = {'use': ''}#伪装回调数据其实成功后不需要

            if request.POST.get('userid'):  #接受删除数据信息
                useridnum = request.POST.get('userid')
                print(useridnum)
                run = rpc_cilent.Data()
                for i in useridnum.split(','):
                    sdata = run.dele_data('d','userid',int(i),'0')
                if sdata == 0:
                    art = notice.models.TbUser.objects.order_by("-userid")
                    cust6 = notice.fenye.split_page(art, request, per_page=15)
                    data_user = {'use': cust6}
                    data = {'use': ''}  # 伪装回调数据其实成功后不需要
                else:
                    return JsonResponse({'error': '删除失败'+str(sdata)}, safe=False)
            else:
                data={'erro':'未获取到数据'}
            return JsonResponse(data,safe=False)
        else:
            pass
    else:
        pass
def chaxun_user(request):  #返回人员页面axaj数据的回调页面
    return render(request,'notice/sreach/user-sreach.html',data_user)


def user_add(request):  #空白新增人员视图
    addid = notice.models.Addpath.objects.all()
    zjtype = notice.models.TbDict.objects.filter(item ='zjtype')
    data ={'use':addid,'zjt':zjtype}
    return render(request,'notice/append-html/user-add.html',data)


def append_user(request):  #提交新增人员视图
    if request.method == 'POST':
        if request.is_ajax():
            if request.POST.get('username'):
                appenduser_data ={
                'username' :request.POST.get('username'),
                'sex' : request.POST.get('sex'),
                'mobile': request.POST.get('phone'),
                'zjtype': request.POST.get('zjtype'),
                'zjnum': request.POST.get('zjnum'),
                'placeid': request.POST.get('addaes'),
                'address': request.POST.get('address')
                }
                run = rpc_cilent.Data()
                sdata = run.newuser(appenduser_data)
                if sdata ==0:
                    return JsonResponse({'type': '新增完成'}, safe=False)
                else:
                    return JsonResponse({'error': '缺少用户名'}, safe=False)

            else:
                return JsonResponse({'error':'缺少用户名'},safe=False)

def loudong_list(request):  #楼栋视图
    addid = notice.models.Addpath.objects.all()
    data = {'use': addid}
    return render(request, 'notice/loudong-list.html', data)

