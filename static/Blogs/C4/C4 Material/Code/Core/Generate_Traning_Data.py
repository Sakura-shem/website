import json
# 数据范围：
# 	脉搏每分钟次数：40～120
# 	声音每分钟均值：20~100
# 	专注度：0~1024
# 	眨眼每分钟：10~30

#数据格式：
#   [脉搏数 ， 眨眼数 ， 声音大小 ，专注度]

#一个文件 十组数据
#十次调用 两个文件
#一共要100个文件

def Generate_Traning_Data_File(Safe_Traning_Data , Fatigue_Traning_Data , i):
    path = ['D:\Document\Creat\magic\Python\C4\Data\\Training_Data\\Safe_' + i +".json" , 'D:\Document\Creat\magic\Python\C4\Data\\training_data\\Fatigue_' + i +".json"]
    f = open(file = path[0] ,   mode = "w" )
    json.dump(Safe_Traning_Data, f)
    f.close()
    f = open(file = path[1] , mode = "w")
    json.dump(Fatigue_Traning_Data, f)
    f.close()