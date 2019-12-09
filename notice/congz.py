import dj_sqlconn
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import datetime
from dateutil.relativedelta import relativedelta

cong=[]
def congzh(request):
    conn1=dj_sqlconn.sql_conn()
    cursor=conn1.cursor()
    global cong
    if request.method=='POST' :
        carnum=request.POST.get('carnum').strip()
        feeid=request.POST.get('feeid').strip()
        date=request.POST.get('date').strip()
        datanum=request.POST.get('datanum').strip()
        if request.POST.get('tijiao', '') == '提交':
            cursor.execute('''SELECT expired1, expired2 FROM bsznpark.dbo.tb_car where carnum ='%s' ''' % carnum)
            rows=cursor.fetchone()
            if rows:
                ex1=int(rows[0])
                ex2=int(rows[1])
                if ex1 >= 0 and ex2 >= 0:
                    html = "<html><body><script> {% window.alert(没有空闲充值窗口，不能充值);%} </script></body></html>"
                    return HttpResponse(html)
                if date=='':
                    html = "<html><body>请输入开始日期</body></html>"
                    return HttpResponse(html)
                if datanum =='':
                    html = "<html><body>请输入充值月数</body></html>"
                    return HttpResponse(html)
                if feeid =='':
                    feeid=11
                else:
                    carp = carnum
                    t1 = datetime.datetime.strptime(str(date), '%Y-%m-%d')      #将str日期转化为datetime格式
                    month_ago1 = t1 + relativedelta(months=int(datanum))      #计算几个月之后的日期
                    month_ago=month_ago1.strftime("%Y-%m-%d")   #再将datetime格式转化为str日期
                    cursor.execute(
                      '''SELECT monthprice ,month3cut , month6cut, month12cut FROM bsznpark.dbo.tb_parkprice where priceid ='%s' ''' % feeid)
                    rowa=cursor.fetchone()
                    mon=rowa[0]
                    mon3=rowa[1]
                    mon6=rowa[2]
                    mon12=rowa[3]
                    if date<'3':
                        fei=int(datanum)*int(mon)
                        feicut=0
                    if '6'>date>='3':
                        fei=int(datanum)*int(mon)-int(mon3)
                        feicut=int(mon3)
                    if '12'>date>='6':
                        fei = int(datanum)*int(mon) - int(mon6)
                        feicut =int(mon6)
                    if date>='12':
                        fei = int(datanum)*int(mon) - int(mon12)
                        feicut =int(mon12)
                    cong=[carnum,feeid,date,datanum,month_ago,feicut,fei]
                    cursor.execute(
                        '''SELECT begin1 ,end1 , begin2, end2 FROM bsznpark.dbo.tb_car where carnum ='%s' ''' % carnum)
                    ra=cursor.fetchone()
            else:
              html = "<html><body>您输入的车牌不是月保车辆</body></html>"
              return HttpResponse(html)

        if request.POST.get('chongzhi', '') == '确认充值':
            aut = cong
            if not aut:
                html = "<html><body>信息不全不能充值</body></html>"
                return HttpResponse(html)
            else:
                params = (str(aut[0]), 0, 2, 0, 'WEB', str(aut[2]), str(aut[4]), int(aut[6]), int(aut[1]))
                cursor.execute("""
                                   DECLARE	@return_value int,
                                           @autoid1 int
                                   SELECT	@autoid1 = -1
                                   EXEC    @return_value = [dbo].[pr_savemcarfeebycarnum]
                                           @carnum = '%s',
                                           @officeid = %d,
                                           @officetype =%d,
                                           @dutyid =%d,
                                           @opname ='%s',
                                           @expbegin ='%s',
                                           @expend = '%s',
                                           @fee =%d,
                                           @autoid = @autoid1 OUTPUT,
                                           @mpriceid =%d             
                                   SELECT  @autoid1             
                                   """ % tuple(params))
                ro = cursor.fetchone()
                conn1.commit()
                print(ro[0])
                html = "<html><body>充值成功，收费记录号:%s</body></html>" % ro[0]
                return HttpResponse(html)
    else:
        return render(request, 'notice/congz.html')
    conn1.close()
    return render(request, 'notice/congz.html', {'aut': cong,'ra':ra,'ex1':ex1,'ex2':ex2})

