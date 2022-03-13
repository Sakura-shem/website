import math
import os
from re import escape
import sys
path = os.path.dirname(__file__) # 模块所在文件夹的绝对路径
sys.path.append(path)
from TreePlotter import *
import Get_Data , Deal_Data
import time

#数据集 和 特征列表
def CreateDataSet():
    #模型构建测试测试数据集
    
    # #原始数据集
    # DataSet = [
    #     [70 , 30 , 'Safe'],
    #     [60 , 50 , 'Safe'],
    #     [70 , 30 , 'Safe'],
    #     [60 , 50 , 'Safe'],
    #     [70 , 30 , 'Safe'],
    #     [60 , 50 , 'Safe'],
    #     [70 , 30 , 'Safe'],
    #     [60 , 50 , 'Safe'],
    # ]
    
    # #数据集中不能有特殊的数
 
    # #概率化后的数据集
    # #对应 脉搏快，脉搏慢，眨眼快，眨眼慢，声音大，声音小，专注，不专注的概率
    # DataSet1 = [[0.2, 0.8, 0.3, 0.7, 'Safe'], 
    #             [0.25, 0.75, 0.15, 0.85, 'Fatigue'],
    #             [0.2, 0.8, 0.4, 0.6, 'Fatigue'],
    #             [0.25, 0.75, 0.38, 0.62, 'Safe'],
    #             [0.42, 0.58, 0.44, 0.56, 'Safe'],
    #             [0.82, 0.18, 0.44, 0.56, 'Fatigue'],
    #             [0.42, 0.58, 0.64, 0.36, 'Safe'],
    #             [0.82, 0.18, 0.54, 0.46, 'Safe'],
    #             [0.22, 0.78, 0.3, 0.7, 'Fatigue'],
    #             [0.42, 0.58, 0.15, 0.85, 'Fatigue'],
    #             [0.82, 0.18, 0.4, 0.6, 'Safe'],
    #             [0.2, 0.8, 0.38, 0.62, 'Fatigue'],
    #             [0.42, 0.58, 0.64, 0.36, 'Fatigue'],
    #             [0.22, 0.78, 0.54, 0.46, 'Safe'],
    #             [0.2, 0.8, 0.15, 0.85, 'Safe'],
    #             [0.42, 0.58, 0.54, 0.46, 'Fatigue'],
    #             ]
 
    # #概率化--对应安全【隶属函数】
    # DataSet2 = [[0.4, 0.5], #对应脉搏数，眨眼数安全的概率
    #             [0.63, 0.45],
    #             [0.33, 0.55],
    #             [0.83, 0.45],
    #             [0.37, 0.95],
    #             [0.34, 0.35],
    #             [0.83, 0.25],
    #             [0.93, 0.55],
    #             [0.93, 0.55],
    #             [0.93, 0.55],
    #             [0.33, 0.55],
    #             [0.83, 0.45],
    #             [0.37, 0.95],
    #             [0.34, 0.35],
    #             [0.83, 0.25],
    #             [0.93, 0.55],]
    
    #调用 训练集
    Training_Data_Set = Get_Data.Get_Training_DataSet()
    DataSet1 = Deal_Data.Randomization(Training_Data_Set)
    DataSet2 = Deal_Data.Safe_Randomization(Training_Data_Set)

    # 标签
    Labels = ['Pulse_Quick' , 'Pulse_Slow' , 'Blink_Quick' ,  'Blink_Slow' , 'Sound_Big' , 'Sound_Small' , 'Attention' , "Non_Attention"] # 标签
    Label = ['Pulse', 'Blink' , "Sound" , "Attention"]  
    # change to discrete values
    return DataSet1, DataSet2, Labels, Label
 
tag = [True , True , True , True , True , True , True , True]
tag_n = 8
 
def Calc_Is(Label , Labels , DataSet):
    membership_Total = 0
    membership = 0
    #根据 Label 获得总隶属度的和
    Pos = Labels.index(Label)
    for i in DataSet:  
        membership_Total += i[Pos]
    
    #获取某一类样本的隶属度的和
    for i in DataSet:
        if i[-1] == 'Safe':
            membership += i[Pos]
    
    p = membership / membership_Total
    if p == 0 or p == 1:
        Is = 1
    else:
        Is = p * math.log2(p) + (1-p) * math.log2(1-p)
        Is = -1 * Is
    return Is
 
# 计算数据集对应的信息熵 (需要改)
def calcShannonEnt(Label , Labels , DataSet):
    Pos = Labels.index(Label)
    #计算 I(S)
    Is  = Calc_Is(Label , Labels , DataSet)
    #计算 E(S)
    Es = 0
    #所有隶属度求和
    Ps = 0
    for i in DataSet:
        Ps += i[Pos] 
    #获得新集合--SjfV--所有隶属度相同的取一个出来
    Set = []
    dataDic = {}
    n = 0
    for i in DataSet:
        dataDic[n] = i[Pos]
        n += 1 
    n = len(dataDic) - 1
    n1 = n -1
    dataDic_Copy = dict(dataDic)
    for i in dataDic:
        Set0 = []
        for p in dataDic:
            if i < p :
                if p in dataDic_Copy:
                    if dataDic[i] == dataDic_Copy[p]:
                        Set0.append(p)
                        dataDic_Copy.pop(p)
        if len(Set0) != 0:
            Set0.insert(0 , i)
            Set.append(Set0)
 
    dataDic = {}
    for i in Set:
        Set0 = []
        for p in i:
            Set0.append(DataSet[p])
        dataDic[DataSet[p][Pos]] = Set0
 
    for i in dataDic:
        TempIs = Calc_Is(Label , Labels , dataDic[i])
        TempPs = 0
        for p in dataDic[i]:
            TempPs += p[Pos]
        TempEs = TempPs / Ps * TempIs
        Es += TempEs
    #计算G(s)
    Gs = Is - Es
    return Gs
 
# FID3决策树分类算法
def chooseBestFeatureToSplitID3(DataSet, Labels):
    global tag
    num = len(tag)
    best = 0
    G = []
    check = False
    for i in range(num):
        if tag[i]:
            if not check: #首次得到有效值
                best = i
                G.append(calcShannonEnt(Labels[i], Labels, DataSet))
                check = True
            else:
                t = calcShannonEnt(Labels[i], Labels, DataSet)
                G.append(t)
                if t > G[best]:
                    best = i
        else:
            G.append(0)
    if best % 2 == 0:
        best1 = best + 1
        return best, best1, G[best], G[best1]
    else:
        best1 = best - 1
        return best1, best, G[best1], G[best]
 
def min_(f1, f2): # 比较大小
 
    if f1 < f2:
        return f1
    else:
        return f2
 
# FID3构建树---递归的方式
def CreateTreeFID3(DataSet1, DataSet2, Labels, Label):
    global tag_n
    if tag_n == 0: #如果数据集为空则返回空树
        return {}
    bestFeat1, bestFeat2, G1, G2 = chooseBestFeatureToSplitID3(DataSet1, Labels)  # 获得 最大模糊信息增益 对应特征的位置, 同时获取其对应的信息增益值
    if G1 > G2: # 左边分支作为叶子节点
        pulseFast1 = 0.0
        pulseFast2 = 0.0
        pulseFast3 = 0.0
        lenData = len(DataSet1)
        for i in range(lenData):
            pulseFast1 += DataSet1[i][bestFeat1]
            pulseFast2 += min_(DataSet1[i][bestFeat1], DataSet2[i][bestFeat1 // 2])
            pulseFast3 += min_(DataSet1[i][bestFeat1], 1 - DataSet2[i][bestFeat1 // 2])
        S1 = pulseFast2 / pulseFast1 #XX快，安全的真实度
        S2 = pulseFast3 / pulseFast1 #XX快，疲劳的真实度
        W1 = G1 / (G1 + G2)
        W2 = G2 / (G1 + G2)
        S1_ = int(S1 * 100) / 100.0 # 控制格式，保留小数点后两位
        S2_ = int(S2 * 100) / 100.0
        W1_ = int(W1 * 100) / 100.0
        W2_ = int(W2 * 100) / 100.0
        MyTree = {Label[bestFeat1 // 2]:{'Fast:' + str(W1_): 'Safe:' + str(S1_) + ' Fatigue:' + str(S2_)}} # 确定树的根以及左分支
        if tag_n > 2: # 如果类标签长度大于1，则右分支的生成递归调用该过程
            t = Label[bestFeat1 // 2]
            tag_n -= 2
            tag[bestFeat1] = tag[bestFeat2] = False
            MyTree[t]['Slow:' + str(W2_)] = CreateTreeFID3(DataSet1, DataSet2, Labels, Label)
        else: # 否则右分支也是叶子节点
            pulseFast1 = 0.0
            pulseFast2 = 0.0
            pulseFast3 = 0.0
            lenData = len(DataSet1)
            for i in range(lenData):
                pulseFast1 += DataSet1[i][bestFeat1 + 1]
                pulseFast2 += min_(DataSet1[i][bestFeat1 + 1], DataSet2[i][bestFeat1 // 2])
                pulseFast3 += min_(DataSet1[i][bestFeat1 + 1], 1 - DataSet2[i][bestFeat1 // 2])
            S1 = pulseFast2 / pulseFast1  # XX慢，安全的真实度
            S2 = pulseFast3 / pulseFast1  # XX慢，疲劳的真实度
            S1_ = int(S1 * 100) / 100.0 # 调整格式
            S2_ = int(S2 * 100) / 100.0
            MyTree[Label[bestFeat1 // 2]]['Slow:' + str(W2_)] = 'Safe:' + str(S1_) + ' Fatigue:' + str(S2_) # 确定右分支
        return MyTree # 返回树结构
    else: # 右边分支作为叶节点
        MyTree = {Label[bestFeat1 // 2]: {}} # 确定根节点
        W1 = G1 / (G1 + G2)
        W2 = G2 / (G1 + G2)
        W1_ = int(W1 * 100) / 100.0
        W2_ = int(W2 * 100) / 100.0
        pulseFast1 = 0.0
        pulseFast2 = 0.0
        pulseFast3 = 0.0
        lenData = len(DataSet1)
        for i in range(lenData):
            pulseFast1 += DataSet1[i][bestFeat1 + 1]
            pulseFast2 += min_(DataSet1[i][bestFeat1 + 1], DataSet2[i][bestFeat1 // 2])
            pulseFast3 += min_(DataSet1[i][bestFeat1 + 1], 1 - DataSet2[i][bestFeat1 // 2])
        S1 = pulseFast2 / pulseFast1  # XX慢，安全的真实度
        S2 = pulseFast3 / pulseFast1  # XX慢，疲劳的真实度
        S1_ = int(S1 * 100) / 100.0 #调整格式
        S2_ = int(S2 * 100) / 100.0
        if tag_n > 2: # 如果类标签长度大于1，则左分支需要递归调用该过程
            t = Label[bestFeat1 // 2]
            tag_n -= 2
            tag[bestFeat1] = tag[bestFeat2] = False
            MyTree[t]['Fast:' + str(W1_)] = CreateTreeFID3(DataSet1, DataSet2, Labels, Label)
            MyTree[t]['Slow:' + str(W2_)] = 'Safe:' + str(S1_) + ' Fatigue:' + str(S2_) # 确定右分支
        else: #否则左分支也是叶子节点
            pulseFast1 = 0.0
            pulseFast2 = 0.0
            pulseFast3 = 0.0
            lenData = len(DataSet1)
            for i in range(lenData):
                pulseFast1 += DataSet1[i][bestFeat1]
                pulseFast2 += min_(DataSet1[i][bestFeat1], DataSet2[i][bestFeat1 // 2])
                pulseFast3 += min_(DataSet1[i][bestFeat1], 1 - DataSet2[i][bestFeat1 // 2])
            S1 = pulseFast2 / pulseFast1  # XX快，安全的真实度
            S2 = pulseFast3 / pulseFast1  # XX快，疲劳的真实度
            S1__ = int(S1 * 100) / 100.0
            S2__ = int(S2 * 100) / 100.0
            MyTree[Label[bestFeat1 // 2]]['Fast:' + str(W1_)] = 'Safe:' + str(S1__) + ' Fatigue:' + str(S2__)
            MyTree[Label[bestFeat1 // 2]]['Slow:' + str(W2_)] = 'Safe:' + str(S1_) + ' Fatigue:' + str(S2_)
        return MyTree # 返回树结构

Path = "D:\Document\Creat\magic\Python\C4\core\FID3\Tree.json"
DataSet1, DataSet2, Labels, Label = CreateDataSet()
MyTree = CreateTreeFID3(DataSet1, DataSet2, Labels, Label)
StoreTree(MyTree , Path)
CreatePlot(MyTree)

