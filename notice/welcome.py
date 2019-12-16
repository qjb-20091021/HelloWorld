import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context
import json
import notice
from django.db.models import Max
from notice import models
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
import notice.fenye
import os
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


def member_list(request):  # 用户页面数据，数据和页面分离
    use = notice.models.TbUser.objects.order_by("-userid").values()  # 加values后返回的是字典格式数据就不是结果集了
    use_list = []
    for us in use:  # 每条查询生成一个列表数据，里面装了多个字典，每个字典就是一条数据
        ulist = list(us)
        for u in ulist:
            if u in ['sex', 'placeid', 'usertype', 'zjtype']:
                pass
            else:
                if us[u] == None:
                    us[u] = ''
                else:
                    pass
        us['sex_num'] = us['sex']  # 增加id类，作用是为了弹出框的取值，下面的sex赋值是字符串，不能进行修改
        us['placeid_num'] = us['placeid']
        us['usertype_num'] = us['usertype']
        us['zjtype_num'] = us['zjtype']
        us['sex'] = notice.models.TbDict.objects.filter(item='sex', value=us['sex']).values_list(
            'caption').first()  # valus——list如果查询的结果是一个那么返回一个元组，如果查询的结果有多个那么返回的是结果集，所以在后面加frist可以定位到一个结果，就可以字节返回需要的字符串了；
        us['placeid'] = notice.models.Addpath.objects.filter(placeid=us['placeid']).values_list('pathname').first()
        us['usertype'] = notice.models.TbDict.objects.filter(item='usertype', value=us['usertype']).values_list(
            'caption').first()
        us['zjtype'] = notice.models.TbDict.objects.filter(item='zjtype', value=us['zjtype']).values_list(
            'caption').first()
        use_list.append(us)
    num = notice.models.TbUser.objects.all().count()  # 分页所需的数据总个数
    pageIndex = request.GET.get('page')  # 这里的page对应到表格渲染时设置的pagename，后端必须分页，前端才能实现
    pageSize = request.GET.get('limit')  # 获取前端设置的每页数量
    pageInator = Paginator(use_list, pageSize)  # 产生分页对象
    contacts = pageInator.page(pageIndex)  # 所有的分页总数
    res = []  # 最终返回的结果集合
    for contact in contacts:
        res.append(contact)  # 封装单个分页对象传给前端
    c = {"code": 0, "msg": "传输成功", "count": num, "data": res}  #前端规定的格式
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


def loudong_list(request):  # 楼栋视图
    addid = notice.models.Addpath.objects.order_by("-placeid")
    data = {'use': addid}
    return render(request, 'notice/loudong-list.html', data)


def loudong_add(request):  # 新增楼栋
    addid = notice.models.Addpath.objects.all()
    data = {'addid': addid}
    return render(request, 'notice/append-html/loudong-add.html',data)

data_user ={}
def jxja_chaxunuser(request):   #接受查询人员请求
    global data_user
    if request.method == 'POST':
        if request.is_ajax():
            if request.POST.get('username'):  #按姓名查询
                aa=request.POST.get('username') #按姓名
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

            if request.POST.get('userid'):  #接受人员删除数据信息
                useridnum = request.POST.get('userid')
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

            if request.POST.get('placeid'):  # 接受楼栋删除数据信息
                useridnum = request.POST.get('placeid')
                print(useridnum)
                run = rpc_cilent.Data()
                for i in useridnum.split(','):
                    sdata = run.dele_data('z3', 'placeid', int(i), '0')
                if sdata == 0:
                    data = {'use': ''}  # 伪装回调数据其实成功后不需要
                else:
                    return JsonResponse({'error': '删除失败' + str(sdata)}, safe=False)
            else:
                data={'erro':'未获取到数据'}
            return JsonResponse(data,safe=False)
        else:
            pass
    else:
        pass


def chaxun_user(request):  #返回搜索人员页面axaj数据的回调页面
    return render(request,'notice/sreach/user-sreach.html',data_user)


def user_add(request):  #空白新增人员视图
    addid = notice.models.Addpath.objects.all()
    zjtype = notice.models.TbDict.objects.filter(item ='zjtype')
    data ={'use':addid,'zjt':zjtype}
    return render(request,'notice/append-html/user-add.html',data)


def append_user(request):  #提交新增人员视图
    if request.method == 'POST':
        if request.is_ajax():
            if request.POST.get('username'):  #新增用户数据
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
            if request.POST.get('username1'):  # 修改用户数据
                appenduser_data = {
                    'userid': request.POST.get('userid'),
                    'username': request.POST.get('username1'),
                    'sex': request.POST.get('sex'),
                    'mobile': request.POST.get('phone'),
                    'zjtype': request.POST.get('zjtype'),
                    'zjnum': request.POST.get('zjnum'),
                    'placeid': request.POST.get('addaes'),
                    'address': request.POST.get('address'),
                    'usertype': request.POST.get('usertype'),
                    'opname': request.POST.get('opname')}
                if appenduser_data['sex'] == 'undefined':
                    del appenduser_data['sex']
                else:
                    pass
                run = rpc_cilent.Data()
                sdata = run.modify_user(appenduser_data)
                if sdata == 0:
                    return JsonResponse({'type': '修改完成'}, safe=False)
                else:
                    return JsonResponse({'type': str(sdata)}, safe=False)

            if request.POST.get('loudongname'):  # 新增
                ceid = notice.models.TbPlace.objects.all()
                placenum = ceid.aggregate(Max('placeid'))
                pnum = placenum['placeid__max'] + 1  # 获取最大的placeid再加一
                appenduser_data = {
                    'placename': request.POST.get('loudongname'),
                    'placeid': pnum,
                    'pid': request.POST.get('pid')}
                run = rpc_cilent.Data()
                sdata = run.newloudong(appenduser_data)
                if sdata == 0:
                    return JsonResponse({'type': '修改完成'}, safe=False)
                else:
                    return JsonResponse({'type': str(sdata)}, safe=False)

            else:
                return JsonResponse({'error':'缺少用户名'}, safe=False)


def user_xiugai(request):  # 打开修改人员视图
    addid = notice.models.Addpath.objects.all()  # 想实现视图的模板功能，必须新建model，方法和addpath一样
    zjtype = notice.models.TbDict.objects.filter(item='zjtype')
    usertype = notice.models.TbDict.objects.filter(item='usertype')
    data_xiugai = {'use': addid, 'zjt': zjtype, 'usertype': usertype}
    return render(request, 'notice/append-html/user-xiugai.html',data_xiugai)
