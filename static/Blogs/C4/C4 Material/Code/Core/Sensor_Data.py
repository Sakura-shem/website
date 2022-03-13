import serial
import os
import sys
path = "D:\\Document\\Creat\\magic\\Python\\C4\\core\\Mind_wave"
sys.path.append(path)
from EGG import get_attention

#追加 写 数据
def write_data(path , data , i , conn):
    if i == 0:
        with open (path[0] , "w") as f:
            f.write("%s\n" % data)
    elif 0 < i < 100 :
        with open (path[0] , "a") as f:
            f.write("%s\n" % data)
    #开始 写路径 1 
    elif (i == 100):
        with open (path[1] , "w") as f:
            f.write("%s\n" % data)
            conn.send(0)
    elif 100 < i < 200:
        with open (path[1] , "a") as f:
            f.write("%s\n" % data)
    #开始 写路径 0
    elif i == 200:
        with open (path[0] , "w") as f:
            f.write("%s\n" % data)
        conn.send(1)

# 无声音为 500 、1000为最大声音信号【响度】 
def Get_Data(conn): 
    Pulse_Path = [os.getcwd() + "\\C4\\Data\\Sensor_data\\data\\pluse.txt" , os.getcwd() + "\\C4\\Data\\Sensor_data\\data1\\pluse.txt"]
    Sound_Path = [os.getcwd() + "\\C4\\Data\\Sensor_data\\data\\Sound.txt" , os.getcwd() + "\\C4\\Data\\Sensor_data\\data1\\Sound.txt"]
    Attention_Path  =[os.getcwd() + "\\C4\\Data\\Sensor_data\\data\\Attention.txt" , os.getcwd() + "\\C4\\Data\\Sensor_data\\data1\\Attention.txt"]
    port = "COM3"
    baud_rate = 9600
    audio = serial.Serial(port , baud_rate)
    i = 0
    while(1):
        data = audio.readline().strip()[-8::]
        Pulse_Data = str(data[:3:])[2:5:]
        Sound_Data = str(data[-3::])[2:5:]
        Attention_Data = get_attention()
        write_data(Attention_Data , Attention_Path)
        write_data(Pulse_Path , Pulse_Data , i , conn)
        write_data(Sound_Path , Sound_Data , i , conn)
        i += 1
        if i > 200:
            i = 0