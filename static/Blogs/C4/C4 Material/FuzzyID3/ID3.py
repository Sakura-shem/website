import math
#创建 数据集 和 特征列表
def createDataSet():
    dataSet = [[0, 0, 1, 0, '失败'],
               [0, 0, 1, 1, '失败'],
               [0, 1, 0, 1, '成功'],
               [0, 1, 1, 0, '成功'],
               [0, 0, 0, 0, '失败'],
               [1, 0, 0, 0, '失败'],
               [1, 0, 0, 1, '失败'],
               [1, 1, 1, 1, '成功'],
               [1, 0, 1, 2, '成功'],
               [1, 0, 1, 2, '成功'],
               [2, 0, 1, 2, '成功'],
               [2, 0, 1, 1, '成功'],
               [2, 1, 0, 1, '成功'],
               [2, 1, 0, 2, '成功'],
               [2, 0, 0, 0, '失败']]
    labels = ['age', 'work', 'house', 'credit']
    # change to discrete values
    return dataSet, labels

# 计算数据集对应的香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)   #获得 样本总数【数据集个数】---列表个数
    labelCounts = {}    #创建分类标签变量，键值对形式，结果：结果出现次数
    shannonEnt = 0.0
    for featVec in dataSet:  #统计样本集的 结果,计数并存到字典里
        currentLabel = featVec[-1]  #   取到结果的值
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    for key in labelCounts:                     # 根据 结果出现次数 计算香农熵
        prob = float(labelCounts[key]) / numEntries     # 计算 p(x)--出现结果【某种事件】出现的概率
        shannonEnt -= prob * math.log(prob, 2)  # log base 2
    return shannonEnt

# 按特征和特征值分割数据集--删去原数据集中 不具有某种特征某个值的数据 和 具有特征的数据对应特征--->新数据集
# 数据集 , 特征值所处位置 , 特征对应的值
def splitDataSet(dataSet, axis, value):
    retDataSet = [] #划分完的数据集
    for featVec in dataSet:    #[0, 0, 0, 0, 'no']
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)  # 这里注意extend和append的区别
    return retDataSet

# ID3决策树分类算法---返回 最大信息增益 对应 特征的 所处位置
def chooseBestFeatureToSplitID3(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 求出 所有结果-->对应特征的种类数
    baseEntropy = calcShannonEnt(dataSet) # 计算原始数据集的香农熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 循环选取 每种特征 作为分类，【默认 结果 是列表最后一个元素】
        featList = [example[i] for example in dataSet]  # 取出所有数据的 某个特征---->列表
        uniqueVals = set(featList)  # 【利用集合互斥性】将特征的所有的不同的值---->集合
        newEntropy = 0.0
        for value in uniqueVals:    # 用 特征的所有不同值 分别分割原始数据集，计算信息增益
            subDataSet = splitDataSet(dataSet, i, value)    # 分割原始数据集---原始数集，特征的位置,特征值--->筛选并减轻后的新数据集
            prob = len(subDataSet) / float(len(dataSet))    # 新数据集中数据个数 / 原数据集中数据个数 --->特征某种值的占比
            newEntropy += prob * calcShannonEnt(subDataSet) # 计算条件熵 = Σ 概率 * 子集香农熵
        infoGain = baseEntropy - newEntropy  #  计算 信息增益
        if (infoGain > bestInfoGain):  #    比较 信息增益
            bestInfoGain = infoGain
            bestFeature = i #   获得 最大信息增益对应特征的列表中位置
    return bestFeature  # 返回  位置

# 当所有特征都用完的时 投票决定分类  【未写完】
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    # sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # return sortedClassCount[0][0]

# ID3构建树---迭代的方式
def createTreeID3(dataSet, Labels):
    classList = [example[-1] for example in dataSet]  # 创建类标签,所有结果--->列表
    if classList.count(classList[0]) == len(classList): # 判断 该子类所有结果 是否一致
        return classList[0]  # 如果 结果一致 则停止，直接返回该类标签【子类已经纯了】
    if len(dataSet[0]) == 1:  # 遍历完了所有的标签仍然不能将数据集划分为仅包含唯一类别的分组---列表长度为 1【仅剩结果了】
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplitID3(dataSet)  # 获得 最大信息增益 对应特征的位置
    bestFeatLabel = Labels[bestFeat]  # 根据位置 获得最大信息增益 对应的特征名称--最佳特征
    myTree = {bestFeatLabel: {}}  # 创建 决策树
    del Labels[bestFeat]  # 从label里删掉最佳特征，
    subLabels = Labels  #   创建迭代的label列表
    featValues = [example[bestFeat] for example in dataSet]  # 这个最佳特征对应的所有值--->列表
    uniqueVals = set(featValues)    # 【利用集合互斥性】将特征的所有的不同的值---->集合
    for value in uniqueVals:    # 循环每种值
        myTree[bestFeatLabel][value] = createTreeID3(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


Raw_Data, Labels = createDataSet() #生成 原始数据集
mytree = createTreeID3(Raw_Data, Labels)
print(mytree)

#credit--0
#        1
#        2  
