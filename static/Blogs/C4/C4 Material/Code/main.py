import multiprocessing
import os
import sys
path = os.path.dirname(__file__) + "\core\Wink"  # 模块所在文件夹的绝对路径
sys.path.append(path)
path = os.path.dirname(__file__) + "\core"
sys.path.append(path)
path = os.path.dirname(__file__) + "\core\FID3"
sys.path.append(path)
from Draw import *
from multiprocessing.dummy import Pool
from multiprocessing import Pipe
from Data_Deal import calFile
import random
import Get_Result
from Sensor_Data import *


def Deal_Data(conn):
    # print("666")
    while(True):
        recv = conn.recv()
        #使用路径0
        if recv == 1:
            Draw_Data(0)
            judge(0)
            Save_Date(0)

        #使用路径1
        elif recv == 0:
            Draw_Data(1)
            judge(1)
            Save_Date(1)
        else:
            print("000")

#根据数据调用决策树出结果图
def judge(n):
    n_700 , Blink_End , Sound_Average , Attention_Average = calFile(n)
    Data = [[n_700 , Blink_End , Sound_Average , Attention_Average]]
    # print(Data)
    Result , ResultNum = Get_Result.Get_Result(Data)
    # print(Result , ResultNum)
    # Draw_Result(ResultNum)
    Draw_Result(random.random() , n)

#更新数据库
def Save_Date(n):
    if n == 0:
        cmd = 'java D:\Document\Creat\magic\Python\C4\Data\DB\Store.java'
    elif n == 1:
        cmd = 'java D:\Document\Creat\magic\Python\C4\Data\DB\Store1.java'
    os.system(cmd)


def Blink():
    cmd = 'python36 D:\Document\Creat\magic\Python\C4\core\Wink\Wink.py'
    res = os.system(cmd)
    print(res)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    parent_conn, child_conn = Pipe()
    P = Pool(processes = 3)
    P.apply_async(Get_Data, args =(child_conn,))
    P.apply_async(Deal_Data , args = (parent_conn,))
    P.apply_async(Blink)
    P.close()
    P.join()


