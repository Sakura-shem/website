import os
import pickle
import sys
path = os.path.dirname(__file__) # 模块所在文件夹的绝对路径
sys.path.append(path)
from Deal_Data import *

ResultSort1 = 'Safe' # 全局变量分别记录两条路径当前的最大概率
ResultNum1 = 0.0
ResultSort2 = 'Fatigue'
ResultNum2 = 0.0
def getSort(Data, label, t_front, trees): #data是经过处理后的输入数据，label是标签，t_front是前面路径对应权重之乘积，trees是递归处理的子树
    global ResultNum1
    global ResultSort1
    global ResultNum2
    global ResultSort2

    # Data  = [Data]
    if len(Data) != 1:
        if ResultNum1 > ResultNum2: # 安全
            return ResultSort1, int((ResultNum1 / (ResultNum1 + ResultNum2)) * 100) / 100
        else:
            return ResultSort2, int((ResultNum2 / (ResultNum1 + ResultNum2)) * 100) / 100
    Data = Randomization(Data)
    Data = Data[0]
    
    firstStr = list(trees.keys())[0] # 根节点
    secondDict = trees[firstStr]
    featIndex = label.index(firstStr) * 2 # 得到索引值
    pFast = Data[featIndex] # 获取样本数据对应快和慢的概率
    pSlow = 1 - pFast
    tag = True
    for key in secondDict.keys(): # 分别对左右两个分支进行处理
        if type(secondDict[key]).__name__ == 'dict': # 如果不是叶子节点，则递归处理
            t = 1.0
            if tag: # 左分支不是叶节点
                t = pFast * float(key.strip('Fast:'))
            else:
                t = pSlow * float(key.strip('Slow:'))
            getSort(Data, label, t, secondDict[key])
            tag = False
        else:
            t = 1.0
            s = secondDict[key]
            s1 = s.strip('Safe:')
            s2 = s1.split(' Fatigue:')
            p1 = float(s2[0]) # 求出节点对应的真实度
            p2 = float(s2[1])
            if tag: # 左分支是叶节点
                pSafe = t_front * pFast * float(key.strip('Fast:')) * p1
                pFatigue = t_front * pFast * float(key.strip('Fast:')) * p2
                if pSafe > ResultNum1: # 更新
                    ResultNum1 = pSafe
                if pFatigue > ResultNum2:
                    ResultNum2 = pFatigue
            else:
                pSafe = t_front * pSlow * float(key.strip('Slow:')) * p1
                pFatigue = t_front * pSlow * float(key.strip('Slow:')) * p2
                if pSafe > ResultNum1:  # 更新
                    ResultNum1 = pSafe
                if pFatigue > ResultNum2:
                    ResultNum2 = pFatigue
            tag = False
    if ResultNum1 > ResultNum2: # 安全
        return ResultSort1, int((ResultNum1 / (ResultNum1 + ResultNum2)) * 100) / 100
    else:
        return ResultSort2, int((ResultNum2 / (ResultNum1 + ResultNum2)) * 100) / 100
    
 # 读取决策树, 文件不存在返回None
def GetTree(filename):
    if os.path.isfile(filename):
        fr = open(filename, 'rb')
        return pickle.load(fr)
    else:
        return None

def Get_Result(Data):
    Path = "D:\Document\Creat\magic\Python\C4\core\FID3\Tree.json"
    MyTree = GetTree(Path)
    # print(MyTree)
    Label = ['Pulse', 'Blink' , "Sound" , "Attention"]
    # print(Data)
    Result , ResultNum = getSort(Data, Label, 1, MyTree)
    return Result , ResultNum

if __name__ == "__main__":
    Data = [[80.0 , 60.0 , 20.0 , 555.0]]
    Result , ResultNum = Get_Result(Data)
    print(Result , ResultNum)