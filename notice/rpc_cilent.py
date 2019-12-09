
# .-*- coding:utf-8 .-*-
import os,sys
import time
import pika
import uuid
import demjson
import configparser
from .import rpc_Transfertext
from .import logoing


class Rpc(object):              #rpc客户端
    def __init__(self):
        self.logger = logoing.log()  # 初始化logo模块
        config = configparser.ConfigParser()        #创建配置文件读取对象
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        config.read(parent_dir+"/conf.ini", encoding="utf-8")    #读取配置文件
        self.host = config.get("mq_conf", "host")
        self.port = config.getint("mq_conf", "port")
        self.vhost = config.get("mq_conf", "vhost")
        self.credentials = pika.PlainCredentials(config.get("mq_conf", "user"), config.get("mq_conf", "password"))
        self.Parameters = pika.ConnectionParameters(self.host, self.port, self.vhost, self.credentials, heartbeat=5,
                                                    socket_timeout=10)
        self.connection = pika.BlockingConnection(self.Parameters)  # 创建连接
        self.channel = self.connection.channel()
        result = self.channel.queue_declare('',exclusive=True)     #随机声明广播管道，前面的空是指使用默认路由，因为他是用掉就关的所以都是随机的
        self.callback_queue = result.method.queue            #使用随机命名
        self.channel.basic_consume(on_message_callback=self.body, auto_ack=True,
                                   queue=self.callback_queue)    #消费消息，转到body

    def body(self,ch, method, props, body):    #接受回调消息
        if self.corr_id == props.correlation_id:    #检测是否是自己的消息
            self.response = body
    def conn(self,list):           #发送消息
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',    #默认路由
                              routing_key='new_queue',
                              properties=pika.BasicProperties(
                                  reply_to=self.callback_queue,    #发送到随机管道
                                  correlation_id=self.corr_id,     #id用刚刚生成的id
                              ),
                              body=str(list))  # 发出调用,此消息只接受str，就算是列表，也会变成str，所以要用str转换符
        while self.response is None:  # 这边就相当于阻塞了
            try:
                self.connection.process_data_events()  # 查看回调队列
            except (pika.exceptions.AMQPHeartbeatTimeout,pika.exceptions.StreamLostError,ConnectionResetError,pika.exceptions.AMQPConnectionError) as e:
                print(e)
                continue
        return self.response


class Data():
    def __init__(self):
        self.logger = logoing.log()  # 初始化logo模块
    def pic(self,num,carnum):  #查询图片接口，输入参数为：表代码，车牌
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listsp
        Tranlist[0] = num  #查询的表，e是进出记录表，c是车辆表
        Tranlist[3]['carnum'] = carnum  #查询的车牌
        response = rpc.conn(Tranlist)  #向本地服务器发送消息
        response = response.decode(encoding="utf-8")   #解码二进制数据
        jrow = demjson.decode(response)  #解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == 0:
            print('ok')
        if jrow == '5':
            self.logger.error('tcp传输失败')
        else:
            self.logger.error(jrow)
        return jrow

    def sdata(self,tablenum,column,carnum,opnum):   #查询小数据接口,输入参数为：表代码，字段名称，字段数据，比较符代码直接返回到函数，不进数据库，注意只能返回一条
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listsd
        Tranlist[0] = tablenum  # 查询的表，e是进出记录表，c是车辆表，具体看list文档
        Tranlist[3][column] = carnum  # 查询的车牌,如果键是id号，值必须是int，如果键是var，值是str
        Tranlist[3]['optype'] = opnum  # 查询的比较方式，大于，等于，小于等等，具体看ini文件，注意格式为字符串
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if len(jrow) == 0:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow

    def dele_data(self,tablenum,column,carnum,opnum):   #删除数据
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listdd
        Tranlist[0] = tablenum  # 查询的表，e是进出记录表，c是车辆表，具体看list文档
        Tranlist[3][column] = carnum  # 查询的车牌,如果键是id号，值必须是int，如果键是var，值是str
        Tranlist[3]['optype'] = opnum  # 查询的比较方式，大于，等于，小于等等，具体看ini文件，注意格式为字符串
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow
    def modify_car(self,dict):   #更新车辆信息，参数是需要更新的信息字典，车牌为必填项，更新时var和时间类型必须为字符串，int必须为int
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listmc
        Tranlist[3].update(dict)      #修改的车牌信息，车牌为必填
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow
    def modify_user(self,dict):   #更新人员信息，参数是需要更新的信息字典，userid为必填项，更新时var和时间类型必须为字符串，int必须为int
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listmu
        Tranlist[3].update(dict)      #修改的人员信息，userid为必填
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow

    def recar(self,dict):  #输入充值续期信息，类型为dict，字典项目不能变，注意免费车续期时，fee项不能填，车牌为必填，返回收费记录号，如果为o，则为免费车续期成功，如果为1则发生错误
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listre
        Tranlist[3].update(dict)
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow
    def newcar(self,dict): #新增车辆，车牌为必填，参数类型为dict，如果有车牌重复，则会报错,userid和nusename必须填一样，如果有userid，则不检查其他user信息，如果没有则会新增user项
        rpc = Rpc()      #新增免费车时不能填费用项
        Tranlist = rpc_Transfertext.listnc    #carattr为必填项
        Tranlist[3].update(dict)
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow
    def newuser(self,dict): #新增人员，username为必填，参数类型为dict
        rpc = Rpc()
        Tranlist = rpc_Transfertext.listnu
        Tranlist[3].update(dict)
        response = rpc.conn(Tranlist)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow

    def Upload(self,list):  #更新部分资料，参数类型为列表,第一项时表代码，第三项返回数据数量，0为返回所有，第4项：字典类型，键是查询字段，值是条件值；这个值里只能时int类型的值，有一个必填键值optype；，第6项：删除方式2为删除更新部分，第7项：0，代表是更新事件
        rpc = Rpc()
        response = rpc.conn(list)  # 向本地服务器发送消息
        response = response.decode(encoding="utf-8")  # 解码二进制数据
        jrow = demjson.decode(response)  # 解码json数据，发的时候都是通过json封装发送送的，但在发送的过程中传输的都是二进制数据，所以要先解码二进制
        if jrow == None:
            self.logger.error('tcp传输失败')
        else:
            pass
        return jrow

if __name__ == '__main__':
    while True:
        try:
            run = Data()
            tu = run.sdata('d','userid','123','0')
            print(tu)
            time.sleep(2)
        except pika.exceptions.AMQPConnectionError as e :
            print(e)