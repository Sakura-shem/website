# import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
from scipy.optimize import leastsq
import os
# plt.switch_backend('agg')
# import time
# 载入库
import numpy as np
# import pylab as pl
from PIL import Image




# 定义函数形式和误差
def func(x, p):
    A, k, theta = p
    return A * np.sin(2 * np.pi * k * x + theta)

def residuals(p, y, x):
    return y - func(x, p)

def Gen_Curve():
    # 生成训练数据
    x = np.linspace(0, -2 * np.pi, 100)
    A, k, theta = 10, 0.34, np.pi / 6
    y0 = func(x, [A, k, theta])
    y1 = y0 + 2 * np.random.randn(len(x))

    # trian the para
    p0 = [7, 0.2, 0]  # 在非线性拟合中，初始参数对结果的好坏有很大的影响
    Para = leastsq(residuals, p0, args=(y1, x))
    a1, a2, a3 = Para[0]
    # plot

    # 设置figure_size尺寸
    plt.rcParams['figure.figsize'] = (5.0 , 4.0) 
    #设置图片像素
    plt.rcParams['savefig.dpi'] = 100
    plt.scatter(x, y1, color="red", label="Sample Point", linewidth=3)  # 画样本点
    y = a1 * np.sin(2 * np.pi * a2 * x + a3)
    plt.plot(x, y, color="orange", label="Fitting Line", linewidth=2)  # 画拟合直线
    plt.legend()
    return plt
    # plt.show()

#传入 int 型 疲劳概率
def Draw_Result(Fatigue_Ratio , n): 
    Safety_Ratio = str(1 - Fatigue_Ratio)
    Fatigue_Ratio = str(Fatigue_Ratio)
    path = os.path.dirname(__file__)[:-4:] + "Data"
    Result_Path = [path + '\\images\\Result.jpg' , path + '\\images\\Result1.jpg']
    #占比
    frac = [Fatigue_Ratio , Safety_Ratio]
    #名称
    labels = ['Fatigue' , 'Safety']
    #绘图并保存
    plt.pie(frac,labels=labels,autopct='%.2f%%')#autopct为百分比保留位数
    # 设置figure_size尺寸
    plt.rcParams['figure.figsize'] = (5.0 , 4.0) 
    #设置图片像素
    plt.rcParams['savefig.dpi'] = 100
    plt.savefig(Result_Path[n])
    plt.figure()
    #展示图
    # plt.show()
    
def Draw_Data(n):
    mpl.rc('figure', max_open_warning = 0)
    Path = os.path.dirname(__file__)
    Path = Path[:-4:] + "Data"
    Pluse_File_Path = [os.path.dirname(__file__)[:-5:] + "/Data/Sensor_data/data/Pulse.txt" , os.path.dirname(__file__)[:-5:] + "/Data/Sensor_data/data1/Pulse.txt"]
    Sound_File_Path = [os.path.dirname(__file__)[:-5:] + "/Data/Sensor_data/data/Sound.txt" , os.path.dirname(__file__)[:-5:] + "/Data/Sensor_data/data1/Sound.txt"]
    Attention_File_Path = [os.path.dirname(__file__)[:-5:] + "/Data/Sensor_data/data/Attention.txt" , os.path.dirname(__file__)[:-5:] + "/Data/Sensor_data/data1/Attention.txt"]
    Sound_Pic_Path = [Path + '\\images\\Sound.jpg' , Path + '\\images\\Sound1.jpg']
    Pluse_Pic_Path = [Path + '\\images\\Pulse.jpg' , Path + '\\images\\Pulse1.jpg']
    Attention_Pic_Path  = [Path + '\\images\\Attention.jpg' , Path + '\\images\\Attention1.jpg']
    Sounds = []
    Pluses = []
    Attentions = []
    Times1 = []
    Times2 = []
    Times3 = []

    with open(Sound_File_Path[n],'r') as f1:
        for Sound in f1.readlines():
            Sound = Sound.strip('\n')
            Sounds.append(float(Sound))
    for i in range(len(Sounds)):
        Times1.append(float(i))

    with open(Pluse_File_Path[n] , 'r') as f2:
        for Pluse in f2.readlines():
            Pluse = Pluse.strip('\n')
            Pluses.append(float(Pluse))
    for i in range(len(Pluses)):
        Times2.append(float(i))

    with open(Attention_File_Path[n] , 'r') as f3:
        for Attention in f3.readlines():
            Attention = Attention.strip('\n')
            Attentions.append(float(Attention))
    for i in range(len(Attentions)):
        Times3.append(float(i))
    
    ax = plt.gca()

    plt.plot(Times1 , Sounds , marker='o',label='lost plot')
    plt.title("SOUND" , fontsize = 24 )
    # plt.xlabel("t/s")
    # plt.ylabel("db")  
    plt.xlim(-0.5,100)
    plt.ylim(0,150)
    # plt.show()
    # 设置figure_size尺寸
    plt.rcParams['figure.figsize'] = (5.0 , 4.0) 
    #设置图片像素
    plt.rcParams['savefig.dpi'] = 100
    plt.savefig(Sound_Pic_Path[n])
    plt.figure()
    
    
    plt.plot(Times2, Pluses, marker='o', label='lost plot')  # s是点的大小
    plt.title("PLUSE" , fontsize=24)
    plt.xlabel("t/s")
    plt.ylabel("pluse_size")
    plt.xlim(-0.5 , 100)
    plt.ylim(400 , 900)
    #plt.show()
    # 设置figure_size尺寸
    plt.rcParams['figure.figsize'] = (5.0 , 4.0) 
    #设置图片像素
    plt.rcParams['savefig.dpi'] = 100
    plt.savefig(Pluse_Pic_Path[n])
    plt.figure()

    plot = Gen_Curve()
    #plt.show()
    # 设置figure_size尺寸
    plot.rcParams['figure.figsize'] = (5.0 , 4.0) 
    #设置图片像素
    plot.rcParams['savefig.dpi'] = 100
    plot.savefig(Attention_Pic_Path[n])
    plot.figure()

if __name__ == '__main__':
   
    img_switch = Image.open("D:\Document\Creat\magic\Python\C4\Data\Images\Blink1.jpg") # 读取图片
    img_deal = img_switch.resize((500 , 400),Image.ANTIALIAS) # 转化图片
    img_deal = img_deal.convert('RGB') # 保存为.jpg格式才需要
    img_deal.save("D:\Document\Creat\magic\Python\C4\Data\Images\Blink1.jpg")


