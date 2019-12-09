import dj_sqlconn
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import datetime
from dateutil.relativedelta import relativedelta

conn1=dj_sqlconn.sql_conn()
cursor=conn1.cursor()
cong=[]
def mianfeex(request):
    global cong
    global ex1
    global ex2
    if request.method=='POST' :
        carnum=request.POST.get('carnum').strip()
        date=request.POST.get('date').strip()
        datanum=request.POST.get('datanum').strip()
        if request.POST.get('tijiao', '') == '提交':
            cursor.execute('''SELECT expired1, expired2 FROM bsznpark.dbo.tb_car where carnum ='%s' ''' % carnum)
            rows=cursor.fetchone()
            if rows:
                ex1=int(rows[0])
                ex2=int(rows[1])
                if ex1 >= 0 and ex2 >= 0:
                    html = "<html><body>没有空闲续期窗口，不能续期</body></html>"
                    return HttpResponse(html)
                if date=='':
                    html = "<html><body>请输入开始日期</body></html>"
                    return HttpResponse(html)
                if datanum =='':
                    html = "<html><body>请输入续期月数</body></html>"
                    return HttpResponse(html)
                else:
                    carp = carnum
                    t1 = datetime.datetime.strptime(str(date), '%Y-%m-%d')      #将str日期转化为datetime格式
                    month_ago1 = t1 + relativedelta(months=int(datanum))      #计算几个月之后的日期
                    month_ago=month_ago1.strftime("%Y-%m-%d")   #再将datetime格式转化为str日期
                    cong=[carnum,date,datanum,month_ago]
                    cursor.execute(
                        '''SELECT begin1 ,end1 , begin2, end2 FROM bsznpark.dbo.tb_car where carnum ='%s' ''' % carnum)
                    ra=cursor.fetchone()
            else:
              html = "<html><body>您输入的车牌不是免费车辆</body></html>"
              return HttpResponse(html)

        if request.POST.get('chongzhi', '') == '确认充值':
            aut = cong
            if not aut:
                html = "<html><body>信息不全不能续期</body></html>"
                return HttpResponse(html)
            else:
                if ex1 > ex2:
                    cursor.execute("""update bsznpark.dbo.tb_car
                                      set begin2='%s',
                                          end2='%s'
                                      where carnum='%s'                                       
                                       """ % (aut[1],aut[3],aut[0]))
                else:
                    cursor.execute("""update bsznpark.dbo.tb_car
                                                          set begin1 ='%s',
                                                              end1 ='%s'
                                                          where carnum ='%s'
                                       """ % (aut[1], aut[3], aut[0]))
            conn1.commit()
            html = "<html><body>续期成功</body></html>"
            return HttpResponse(html)
    else:
        return render(request, 'notice/mianfee.html')
    return render(request, 'notice/mianfee.html', {'aut': cong,'ra':ra,'ex1':ex1,'ex2':ex2})

