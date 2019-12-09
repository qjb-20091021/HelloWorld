import pymssql
def sql_conn():
    try:
        codeing = 'utf8'
        database1 = 'bsznpark'
        server_name = '127.0.0.1'
        user_name = 'sa'
        password_st = 'sa123-'
        conn1 = pymssql.connect( server=server_name, user=user_name,
                               password=password_st, database=database1,charset=codeing,as_dict=True)
    except Exception:
        print('创建连接失败，请检查数据库信息\n')
    else:
        print('创建连接成功\n')

    return conn1


conn=sql_conn()
cursor = conn.cursor()
cursor.execute('''SELECT column_name,data_type FROM [INFORMATION_SCHEMA].[COLUMNS] where table_name = 'tb_car' and data_type = 'int'
 ''' )
row=cursor.fetchall()
for x in row:

    print(x)