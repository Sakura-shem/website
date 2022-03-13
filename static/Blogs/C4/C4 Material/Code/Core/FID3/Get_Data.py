import json

def Get_Training_DataSet():
    Training_Data_Set = []
    for i in range(5):
        i = str(i)
        path = ['D:\Document\Creat\magic\Python\C4\Data\\Training_Data\\Safe_' + i +".json" , 'D:\Document\Creat\magic\Python\C4\Data\\Training_Data\\Fatigue_' + i +".json"]
        f = open(file = path[0] , mode = "r")
        #反序列化
        Training_Data_Set.append(json.load(f))
        f.close()
        f = open(file = path[1] , mode = "r")
        #反序列化
        Training_Data_Set.append(json.load(f))
        f.close()
    return Training_Data_Set
def Get_Verify_DataSet():
    Verify_DataSet = []
    for i in range(50):
        i = str(i)
        path1 = ['D:\Document\Creat\magic\Python\C4\Data\\Verify_Data\\Safe_' + i +".json" , 'D:\Document\Creat\magic\Python\C4\Data\\Verify_Data\\Fatigue_' + i +".json"]
        f = open(file = path1[0] , mode = "r")
        #反序列化
        Verify_DataSet.append(json.load(f))
        f.close()
        f = open(file = path1[1] , mode = "r")
        #反序列化
        Verify_DataSet.append(json.load(f))
        f.close()
    return Verify_DataSet

if __name__  == "__main__":
    Training_Data_Set = Get_Training_DataSet()
    print(Training_Data_Set)