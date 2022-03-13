from os import path
import os

#应该统计一分钟的数据，然后计算。
#鉴于文件大小，取10s的数据，放大后计算
def calFile(n):
    Path = os.path.dirname(__file__)
    Path = Path[:-4:] + "Data/Sensor_data/"
    Pulse_File_Path = [Path + "data/Pulse.txt" , Path + "data1/Pulse.txt"]
    Sound_File_Path = [Path + "data/Sound.txt" , Path + "data1/Sound.txt"]
    Blink_File_Path = Path + "Blink.txt"
    Attention_File_Path = [Path + "data/Attention.txt" , Path + "data1/Attention.txt"]
    n_700 = 0
    Sum = 0.0
    n_all = 0

    fp = open(Pulse_File_Path[n])  
    while True:
        line = fp.readline()
        if line:
            if float(line) > 700.0:
                n_700 += 1
        else:
            break
    n_700 = float(n_700) * 14

    fp = open(Blink_File_Path)  
    lines = fp.readlines()
    Blink_End = float(lines[-1].strip()) * 4
    

    fp = open(Sound_File_Path[n])  
    while True:
        line = fp.readline()
        if line:
            if line:
                Sum += float(line)
                n_all += 1
        else:
            break
    Sound_Average = Sum / n_all
    Sum = 0.0
    n_all = 0
    
    fp = open(Attention_File_Path[n])
    while True:
        line = fp.readline()
        if line:
            #print(float(line))
            Sum += float(line)
            n_all += 1
        else:
            break
    Attention_Average = Sum / n_all
    
    return n_700 , Blink_End , Sound_Average , Attention_Average

if __name__ == "__main__":
    # ['Pulse', 'Blink' , "Sound" , "Attention"]
    n_700 , Blink_End , Sound_Average , Attention_Average = calFile(0)
    result = [n_700 , Blink_End , Sound_Average , Attention_Average]
    print(result)