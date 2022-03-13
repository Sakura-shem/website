import pymysql
#连接数据库，创建连接对象connection
#连接对象作用是：连接数据库、发送数据库信息、处理回滚操作（查询中断时，数据库回到最初状态）、创建新的光标对象
import os

def clear():
    path = os.path.dirname(__file__)
    print(path[:-4:])
    db = pymysql.connect(host = 'localhost' #host属性
                                ,user = 'root' #用户名 
                                ,password = 'DB666SHEM'  #此处填登录数据库的密码
                                ,db = 'c4' #数据库名
                                )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute("delete from blink where id<>0;")
    cursor.execute("delete from pulse where id<>0;")
    cursor.execute("delete from attention where id<>0;")
    cursor.execute("delete from sound where id<>0;")
    db.commit()
    db.close()# 关闭数据库连接

def show():
    path = os.path.dirname(__file__)
    print(path[:-4:])
    DB = pymysql.connect(host = 'localhost' #host属性
                                ,user = 'root' #用户名 
                                ,password = 'DB666SHEM'  #此处填登录数据库的密码
                                ,db = 'c4' #数据库名
                                )
    # 使用 cursor() 方法创建一个游标对象 cursor
    conn = DB  # "oceantest"
    with conn.cursor() as cursor:
        sql = "select * from Pulse"  # 在test表中取出十条数据
        cursor.execute(sql)
        Result = cursor.fetchall()
    print(Result)
    DB.commit()
    DB.close()# 关闭数据库连接
    	
	
	
	
	
if __name__ == "__main__":
    show()
    clear()