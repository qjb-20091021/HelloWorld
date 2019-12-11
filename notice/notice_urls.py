"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import re_path
from HelloWorld.settings import BASE_DIR
from . import views
from . import congz
from . import mianfee
from . import jinchu
from . import welcome
from django.views.static import serve
import  os
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^congzh/', congz.congzh),
    url(r'^mianfee/', mianfee.mianfeex),
    url(r'^jinchu/', jinchu.jinchux),
    url(r'^jxja/', welcome.jxja_chaxunuser),     #用户表的查询数据接受函数
    url(r'^chaxun-user/', welcome.chaxun_user),   #用户表的查询搜索返回页
    url(r'^user-add/', welcome.user_add),   #新增用户的打开页面
    url(r'^jxja-append-user/', welcome.append_user),  #新增用户的回调函数
    url(r'^indexs/', welcome.indexs),      #前端iframe要对应这里的路由，注意前端的写法是/文件夹/函数/，函数名要登记在这里，例如indexs，并且要保证唯一
    url(r'^shouye/', welcome.shouye),   #首页
    url(r'^member-yemian/', welcome.member_yemian),  # 用户列表页面
    url(r'^member-list/', welcome.member_list, name='member-list'),  # 用户列表页面
    url(r'^fee-list/', welcome.fee_list),
    url(r'^linfee-list/', welcome.linfee_list),
    url(r'^yue-list/', welcome.yue_list),
    url(r'^lin-list/', welcome.lin_list),
    url(r'^mian-list/', welcome.mian_list),
    url(r'^admin-list/', welcome.admin_list),
    url(r'^jilu-list/', welcome.jilu_list),
    url(r'^shijilu-list/', welcome.shijilu_list),
    url(r'^shebei-list/', welcome.shebei_list),
    url(r'^kakou-list/', welcome.kakou_list),
    url(r'^quyu-list/', welcome.quyu_list),
    url(r'^feebz-list/', welcome.feebz_list),
    url(r'^gangting-list/', welcome.gangting_list),
    url(r'^adminlogo-list/', welcome.adminlogo_list),
    url(r'^xianchangsys-list/', welcome.xianchangsys_list),
    url(r'^banfee-list/', welcome.banfee_list),
    url(r'^loudong-list/', welcome.loudong_list),
    re_path(r'^images/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'images')}),   #图片路由
]


