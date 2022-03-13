main.py--项目入口

#Arduino --- 单片机
	module：声音和脉搏模块
	C4：单片机进行脉搏和声音检测

#core --- 核心功能
	wink：眨眼检测
		Capture:摄像头调用
		Wink:眨眼检测
	
	FID3：疲劳分析模型
		Get_Data：训练/验证 数据集调用
		Deal_Data：处理数据【概率化】
		FID3：模型决策树训练
		TreePlotter：模糊决策树 可视化与保存
		Tree：训练完的模型
		Get_Result：训练完模型调用

	Mind_wave：脑波数据采集
		EGG.py：脑波数据采集分析
		mind_wave：专注度数据提取

	Generate_Traning_Data：数据集 采集
	Data_Deal：实时 数据 处理 --->使 处理后数据 可用于 疲劳检测
	Sensor_Data：实时 脉搏和声音传感器数据获取
	Draw：实时 数据及判断结果 可视化
	Db：数据库链接与调用更新

#Data --- 项目数据
	DB：实时 数据 数据库
		Store / Store：将实时数据存入数据库

	Images：实时 数据 和 结果 可视化图片
	Sensor_data：实时 数据 临时保存
	Training_Data：训练集 数据 保存
	Verif_Data：验证集 数据 保存
	
#Web--网页展示
	Ajax：网页动态更新
	Pres:
		images：图片资源
		index：数据展示页
		main：主页入口


