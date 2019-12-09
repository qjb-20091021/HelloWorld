# .-*- coding:utf-8 .-*-
import pymssql
import configparser
import logoing
import os,sys

class Sql():   #本地数据库连接
    def __init__(self):
        self.logger=logoing.log()
    def sql_conn(self):
        try:
            config = configparser.ConfigParser()
            parent_dir = os.path.dirname(os.path.abspath(__file__))
            config.read(parent_dir + "/conf.ini", encoding="utf-8")  # 读取配置文件
            codeing = config.get("sql_conf", "codeing")
            database1 = config.get("sql_conf", "database1")
            server_name = config.get("sql_conf", "server_name")
            user_name =config.get("sql_conf", "user_name")
            password_st = config.get("sql_conf", "password")
            conn1 = pymssql.connect( server=server_name, user=user_name,
                                   password=password_st, database=database1,charset=codeing,as_dict=True)
            #num=pymssql.get_max_connections()  #最大连接数
        except Exception:
            self.logger.warning('创建连接失败，请检查数据库信息\n')
            print('创建连接失败，请检查数据库信息\n')
        else:
            print('创建本地数据库连接成功\n')
        return conn1
class Col():
    def __init__(self):
        sql = Sql()
        self.conn = sql.sql_conn()
        self.columnlist=(( 'int','bit','smallint','money'),( 'varchar','nvarchar'),( 'date','datetime','datetime2','time'))
        config = configparser.ConfigParser()
        config.read("conf.ini", encoding="utf-8")
        self.database = config.get("sql_conf", "database1")

    def jscolumn(self,table_name):   #查询所有计算列
        try:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT sys.computed_columns.object_id,sys.computed_columns.name,sys.all_objects.object_id   
                                FROM sys.computed_columns
                                INNER JOIN sys.all_objects
                                on sys.computed_columns.object_id = sys.all_objects.object_id
                                WHERE sys.all_objects.name = '%s'
                                         ''' % table_name)
        except pymssql.InterfaceError:
            sql = Sql()
            self.conn = sql.sql_conn()
            cursor = self.conn.cursor()
            cursor.execute('''SELECT sys.computed_columns.object_id,sys.computed_columns.name,sys.all_objects.object_id   
                                FROM sys.computed_columns
                                INNER JOIN sys.all_objects
                                on sys.computed_columns.object_id = sys.all_objects.object_id
                                WHERE sys.all_objects.name = '%s'
                                         ''' % table_name)
        finally:
            rows=cursor.fetchall()
        rows_list=[]
        for ro in rows:
            rows_list.append(ro['name'])  #生成计算列字段表
        return rows_list

    def full_column(self,table_name):    #生成除去图片的字段列表
        full_list=[]
        try:
            cursor = self.conn.cursor()
            rows_list = self.jscolumn(table_name)
            cursor.execute('''SELECT table_name,column_name,data_type FROM [INFORMATION_SCHEMA].[COLUMNS] 
                                    where table_name = '%s' and data_type != 'varbinary'
                                     ''' % table_name)
        except pymssql.InterfaceError:
            sql = Sql()
            self.conn = sql.sql_conn()
            cursor = self.conn.cursor()
            rows_list = self.jscolumn(table_name)
            cursor.execute('''SELECT table_name,column_name,data_type FROM [INFORMATION_SCHEMA].[COLUMNS] 
                            where table_name = '%s' and data_type != 'varbinary'
                             '''% table_name )
        finally:
            row=cursor.fetchall()
        for r in row:    #遍历筛选，如果在计算列表里，就不加入输出的字段表
            if r['column_name'] in rows_list:
                pass
            else:
                full_list.append(r['column_name'])
        return full_list


    def int_column(self,table_name,columnstr):    #生成分类字段列表
        rows_list = self.jscolumn(table_name)
        col_list=[]
        try:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT column_name,data_type FROM [INFORMATION_SCHEMA].[COLUMNS] 
                                        where table_name = '%s' and data_type in %s
                                         ''' % (table_name, columnstr))
        except pymssql.InterfaceError:
            sql = Sql()
            self.conn = sql.sql_conn()
            cursor = self.conn.cursor()
            cursor.execute('''SELECT column_name,data_type FROM [INFORMATION_SCHEMA].[COLUMNS] 
                            where table_name = '%s' and data_type in %s
                             '''% (table_name,columnstr) )
        finally:
            row=cursor.fetchall()
        for r in row:  #遍历筛选，如果在计算列表里，就不加入输出的字段表
            if r['column_name'] in rows_list:
                pass
            else:
                col_list.append(r['column_name'])
        return col_list

    def colunm(self,num):   #获取表名
        config = configparser.ConfigParser()
        config.read("conf.ini", encoding="utf-8")
        f = config.get("column", num)
        return f

    def seclt(self,columna,tablena): #生成查询语句
        query = '''SELECT {0} FROM {1}.dbo.{2}  '''
        query = query.format(','.join(columna),self.database,tablena)
        return query

    def keys(self,table_name):  #获取主键
        try:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT
                                    table_name,column_name
                                    FROM
                                    INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
                                    where
                                    table_name = '%s'
                                                ''' % table_name)
        except pymssql.InterfaceError:
            sql = Sql()
            self.conn = sql.sql_conn()
            cursor = self.conn.cursor()
            cursor.execute('''SELECT
                        table_name,column_name
                        FROM
                        INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE
                        where
                        table_name = '%s'
                                    ''' % table_name)
        finally:
            row = cursor.fetchone()
        return row['column_name']

    def itentity(self):   #生成带标识键的表名列表
        itenlist=[]
        try:
            cursor = self.conn.cursor()
            cursor.execute(''' SELECT sys.all_columns.name,sys.all_objects.name
                                        FROM sys.all_columns
                                        INNER JOIN sys.all_objects
                                        on sys.all_columns.object_id = sys.all_objects.object_id
                                        WHERE sys.all_columns.is_identity = 1 ''')
        except pymssql.InterfaceError:
            sql = Sql()
            self.conn = sql.sql_conn()
            cursor = self.conn.cursor()
            cursor.execute(''' SELECT sys.all_columns.name,sys.all_objects.name
                            FROM sys.all_columns
                            INNER JOIN sys.all_objects
                            on sys.all_columns.object_id = sys.all_objects.object_id
                            WHERE sys.all_columns.is_identity = 1 ''')
        finally:
            t=cursor.fetchall()
        for row in t:
            itenlist.append(row['name'])
        return itenlist

    def shuchu(self,num):   #调这个函数产生去掉图片列的查询语句
        sql=self.seclt(self.full_column(self.colunm(num)),self.colunm(num))
        return sql

    def shuchulist(self,num,t):  #调用这个函数获取字段列表
        collist=self.int_column(self.colunm(num),self.columnlist[t])
        return collist

    def shuchukeys(self,num):#调这个函数输出主键
        key=self.keys(self.colunm(num))
        return key

if __name__=='__main__':
    col=Col()
    is_it=col.itentity()
    print(is_it)



