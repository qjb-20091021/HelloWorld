# .-*- coding:utf-8 .-*-
import datetime

listre = ['','','1',{'carnum':'粤BC631Z',
                          'officeid':0,
                          'officetype':2,
                          'dutyid':0,
                          'opname':'web',
                          'expbegin':'2025-1-1',
                          'expend':'2026-1-1',
                          'fee':100,
                          'mpriceid':11},
                          str(datetime.datetime.now()),0,1]    #充值续期的params

listnc = [' ', '', '1', {'carnum':'33333',
                        'carattr':2,
                        },
        str(datetime.datetime.now()), 0,3]  # 新增车辆的params

listnu = [' ', '', '50', {'username': '43333',
                        },
        str(datetime.datetime.now()),0,4]  # 新增人员的params

listdd = ['c', '', '50',
          {
             'optype':'0'
           },
        str(datetime.datetime.now()),0,5]  # 删除数据的params

listsd = ['d', '', '50',
          {
             'optype':'0'
           },
        str(datetime.datetime.now()),0,6]  # 查询小数据的params

listsp = ['c', '', '50',
          {
            'optype': '0'
            },
        str(datetime.datetime.now()), 0, 7]  # 查询照片的params

listmc = ['c', '', '1',
        {
         'carnum':'粤B533ZL'
        },
        str(datetime.datetime.now()),1,2]    #修改车辆信息的params

listmu = ['d', '', '1',
        {
         'userid': 55
         },
        str(datetime.datetime.now()),1,2]  #修改人员资料params
