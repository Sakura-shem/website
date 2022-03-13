# Command line parameters
# python Wink.py --shape-predictor shape_predictor_68_face_landmarks.dat --video your videoname.mp4
# python Wink.py --shape-predictor shape_predictor_68_face_landmarks.dat

#刘海会影响脸部识别效果！！！

# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import keyboard
import os
import sys
import random
path = "D:\\Document\\Creat\\magic\\Python\\C4\\core"
sys.path.append(path)
from Draw import *

#0~1000随机变化、一次最大变化范围100
def create_sound(initial):
    num = random.randint(initial - 100 , initial + 100)
    return num

def create_heart(status):
    if status != 0:
        num = random.randint(450 , 500)
    else:
        num = random.randint(650 , 850)
    return num
    
def sound_heart(i , conn):
    #定义 path 
    Heart_path = [os.path.dirname(__file__)[:-10:] + "/Data/Sensor_data/data/Pluse.txt" , os.path.dirname(__file__)[:-10:] + "/Data/Sensor_data/data1/Pluse.txt"]
    Sound_path = [os.path.dirname(__file__)[:-10:] + "/Data/Sensor_data/data/Sound.txt" , os.path.dirname(__file__)[:-10:] + "/Data/Sensor_data/data1/Sound.txt"]
    write_data(Sound_path , create_sound(300) , i)
    write_data(Heart_path , create_heart(i%10) , i)

def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of vertical eye landmarks (x, y)-coordinates
    # 计算两组垂直眼界标（x，y）坐标之间的欧几里得距离
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal eye landmark (x, y)-coordinates
    # 计算水平眼界标（x，y）坐标之间的欧几里得距离
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio 计算眼睛长宽比
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio 返回眼睛长宽比
    return ear

#追加 写 数据
def write_data(path , data , i):
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
    elif 100 < i < 200:
        with open (path[1] , "a") as f:
            f.write("%s\n" % data)
    #开始 写路径 0
    elif i == 200:
        with open (path[0] , "w") as f:
            f.write("%s\n" % data)

#无限运行
def Wink():
    i = 0
    Num = 0
    #定义每分钟眨眼次数输出路径 和 特征库 位置
    path = [os.path.dirname(__file__)[:-10:] + "/Data/Sensor_data/Blink.txt" , os.path.dirname(__file__)[:-10:] + "/Data/Sensor_data/Blink.txt"]
    dat_path = os.path.dirname(__file__) + "/shape_predictor_68_face_landmarks.dat" #修改
    # define two constants, one for the eye aspect ratio to indicate
    # blink and then a second constant for the number of consecutive frames the eye must be below the threshold
    # 定义两个常数，一个常数表示眼睛的纵横比以指示眨眼，然后定义第二个常数表示眼睛的连续帧数必须低于阈值
    EYE_AR_THRESH = 0.25
    EYE_AR_CONSEC_FRAMES = 2

    # initialize the frame counters and the total number of blinks 初始化帧计数器和闪烁总数
    COUNTER = 0
    TOTAL = 0

    # initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
    # 初始化dlib的面部检测器（基于HOG），然后创建面部界标预测器
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    #参数事dlib库 需要的人脸识别的68个特征点检测库dat文件 的路径
    # print(dat_path)
    predictor = dlib.shape_predictor(dat_path)

    # grab the indexes of the facial landmarks for the left and right eye, respectively
    # 分别获取左眼和右眼的面部标志的索引
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    # start the video stream thread 启动视频流线程
    print("[INFO] starting video stream thread...")
    # vs = FileVideoStream(args["video"]).start()
    fileStream = True
    #内置摄像头或USB摄像头，取消注释：# vs = VideoStream(src=0).start()。
    #Raspberry Pi相机模块，取消注释：# vs = VideoStream(usePiCamera=True).start()。
    #如果您未注释上述两个，你可以取消注释# fileStream = False以及以表明你是不是从磁盘读取视频文件。
    vs = VideoStream(src=0).start()
    #vs = VideoStream(usePiCamera=True).start()
    # fileStream = False

    # time.sleep(1.0)

    start = time.localtime()
    start_t = time.mktime(start)
    # loop over frames from the video stream 循环播放视频流中的帧
    while True:
        # if this is a file video stream, then we need to check if there any more frames left in the buffer to process
        # 如果这是文件视频流，那么我们需要检查缓冲区中是否还有剩余的帧要处理
        # if fileStream and not vs.more():
        #     break

        # grab the frame from the threaded video file stream, resize it, and convert it
        # to grayscale channels)
        # 从线程视频文件流中抓取帧，调整其大小，然后将其转换为灰度通道）
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale frame 在灰度框中检测人脸
        rects = detector(gray, 0)
        
        # loop over the face detections 循环人脸检测
        for rect in rects:
            # determine the facial landmarks for the face region, then convert
            # the facial landmark (x, y)-coordinates to a NumPy array
            # 确定面部区域的面部界标，然后将面部界标（x，y）坐标转换为NumPy数组
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # extract the left and right eye coordinates, then use the coordinates to compute the eye aspect ratio for both eyes
            # 提取左眼和右眼坐标，然后使用坐标计算两只眼睛的眼睛纵横比
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            # average the eye aspect ratio together for both eyes 将两只眼睛的眼睛纵横比平均在一起
            ear = (leftEAR + rightEAR) / 2.0

            # compute the convex hull for the left and right eye, then visualize each of the eyes
            # 计算左眼和右眼的凸包，然后可视化每只眼睛
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # check to see if the eye aspect ratio is below the blink threshold, and if so, increment the blink frame counter
            # 检查眼睛宽高比是否低于眨眼阈值，如果是，则增加眨眼帧计数器
            if ear < EYE_AR_THRESH:
                COUNTER += 1

            # otherwise, the eye aspect ratio is not below the blink threshold
            # 否则，眼睛纵横比不低于眨眼阈值
            else:
                # if the eyes were closed for a sufficient number of then increment the total number of blinks
                # 如果闭上眼睛的次数足够多，则增加眨眼的总数
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    TOTAL += 1

                # reset the eye frame counter 重置眼框计数器
                COUNTER = 0
           
            # # draw the total number of blinks on the frame along with the computed eye aspect ratio for the frame
            # # 绘制帧上眨眼的总数以及计算出的帧的眼睛纵横比
            cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30) , cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0, 0, 255) , 2)
            cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30) , cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0, 0, 255) , 2)
            cv2.putText(frame, "COUNTER: {}".format(COUNTER), (140, 30) , cv2.FONT_HERSHEY_COMPLEX , 0.7 , (0, 255, 255) , 2)

            end = time.localtime()
            end_t = time.mktime(end)
            run_time = end_t -  start_t
            if Num == 0:
                i = 0
            else:
                i = 1
            if run_time == 10:
                write_data(path , TOTAL , i)
                start = time.localtime()
                start_t = time.mktime(start)
                Num += 1
            if Num == 4:
                write_data(path , TOTAL , i)
                TOTAL = 0
                start = time.localtime()
                start_t = time.mktime(start)
                Num = 0 
        # show the frame show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(20) & 0xFF
        #Q键退出
        if keyboard.is_pressed("Q"):
            break
    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

if __name__ == '__main__':
    Wink()