def Pluse_Func(Num):
    P = (1 / 80 * Num) - 0.5 
    return P
def Wink_Func(Num):
    P = (1 / 20 * Num) - 0.5
    return P
def Sound_Func(Num):
    P = (1 / 80 * Num) - 0.25
    return P
def Attention_Func(Num):
    P = Num / 1024
    return P

# [[80.0 , 60.0 , 20.0 , 555.0]]
def Randomization(DataSet):

    # print(DataSet , "777")
    DataSet1 = []
    # [80.0 , 60.0 , 20.0 , 555.0]
    for i in DataSet:
        Temp_Set = []
        Num = 5
        # print(i , "666")
        if len(DataSet) == 1:
            Num = 4
        # print(i)
        # 0 1 2 3
        for n in range(Num):
            if n == 0:
                # print(i[n])
                P = Pluse_Func(i[n])
                Temp_Set.append(round(P , 2))
                Temp_Set.append(round(1-P , 2))
            elif n == 1:
                P = Wink_Func(i[n])
                Temp_Set.append(round(P , 2))
                Temp_Set.append(round(1-P , 2))
            elif n == 2:
                P = Sound_Func(i[n])
                Temp_Set.append(round(P , 2))
                Temp_Set.append(round(1-P , 2))
            elif n == 3:
                P = Attention_Func(i[n])
                Temp_Set.append(round(P , 2))
                Temp_Set.append(round(1-P , 2))
            elif n == 4:
                Temp_Set.append(i[n])
        DataSet1.append(Temp_Set)
    return DataSet1

def Pluse_Safe_Func(Num):
    if Num == 80:
        P = 1
    else:
        P = abs(Num - 80) / 40 
    return P
def Wink_Safe_Func(Num):
    if Num == 20:
        P = 1
    else:
        P = abs(Num - 20) / 10 
    return P
def Sound_Safe_Func(Num):
    if Num == 60:
        P = 1
    else:
        P = abs(Num - 60) / 40 
    return P
def Attention_Safe_Func(Num):
    if Num == 512:
        P = 1
    else:
        P = abs(Num - 512) / 512 
    return P

def Safe_Randomization(DataSet):
    DataSet2 = []
    for i in DataSet:
        Temp_Set = []
        for n in range(4):
            if n == 0:
                P = Pluse_Safe_Func(i[n])
                Temp_Set.append(round(P , 2))
            elif n == 1:
                P = Wink_Safe_Func(i[n])
                Temp_Set.append(round(P , 2))
            elif n == 2:
                P = Sound_Safe_Func(i[n])
                Temp_Set.append(round(P , 2))
            elif n == 3:
                P = Attention_Safe_Func(i[n])
                Temp_Set.append(round(P , 2))
        DataSet2.append(Temp_Set)
    return DataSet2

if __name__ == "__main__":
    DataSet = [[81, 11, 67, 748, 'Safe'], [89, 18, 45, 398, 'Fatigue'], [83, 12, 60, 709, 'Safe'], [92, 16, 49, 415, 'Fatigue'], [75, 15, 72, 744, 'Safe'], [78, 16, 59, 669, 'Fatigue'], [87, 15, 84, 793, 'Safe'], [73, 19, 60, 486, 'Fatigue'], [85, 16, 59, 766, 'Safe'], [98, 15, 64, 435, 'Fatigue']]
    DataSet1 = Randomization(DataSet)
    DataSet2 = Safe_Randomization(DataSet)
    print(DataSet2)