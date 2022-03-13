import cv2 #pip install opencv

def get_video(url,n=0):# 视频录制保存到本地，Q 键退出，摄像头端口，默认0
    cap = cv2.VideoCapture(n)
    if cap.isOpened():
        codev = cv2.VideoWriter_fourcc(*'MJPG')
        fps = 20.0
        frameSize = (640, 480)
        vedio = cv2.VideoWriter(url , codev, fps, frameSize)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                vedio.write(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) == ord('q'):
                    break
            else:
                break
        vedio.release()
    # 释放对象
    cap.release()
    cv2.destroyAllWindows()

def open_video(url): #本地视频读取
    cap = cv2.VideoCapture(url)
    while(True):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame',frame)
        else:
            print("视频读取完毕或者视频路径异常")
            break
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def cap_video(url):#视频按帧读取，保存图片
    cap = cv2.VideoCapture(url)
    c = 1
    frameRate = 20  #帧间隔
    while(True):
        ret, frame = cap.read()
        if ret:
            if(c % frameRate == 0):
                print("开始截取视频第：" + str(c) + " 帧")
                cv2.imwrite("C4/capture_img/" + str(c) + '.jpg', frame) #文件保存路径
            c += 1
            cv2.waitKey(0)
        else:
            print("所有帧都已经保存完成")
            break
    cap.release()

if ( __name__ == "__main__"): 
    print("╰（‵□′）╯")
   

#使用示例
# get_video("video.avi")
# open_video("video.avi")
# cap_video("video.avi")
