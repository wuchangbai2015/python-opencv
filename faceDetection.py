'''
Haar Cascade Face detection with OpenCV  
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''

import numpy as np # Numpy是Python的一个科学计算的库，提供了矩阵运算的功能
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) # 创建VideoCapture对象，参数为设备索引号，对于笔记本电脑，传0表示使用其内置摄像头
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read() # 读入图像img是一个图片矩阵
    img = cv2.flip(img, -1) # 翻转图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 彩色图像转为灰度图像
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,    
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#画出矩行
        # 第一个参数：img是原图
        # 第二个参数：（x，y）是矩阵的左上点坐标
        # 第三个参数：（x+w，y+h）是矩阵的右下点坐标
        # 第四个参数：（0,255,0）是画线对应的rgb颜色
        # 第五个参数：2是所画的线的宽度
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('video',img) # 图像窗口名字，要显示的图像
    # cv2.waitKey()函数是一个键盘绑定函数（相当于让程序在这里挂起暂停执行），
    # 他接受一个单位为毫秒的时间，它等待指定时间的键盘事件，在指定时间内发生
    # 了键盘事件，程序继续执行，否则必须等到时间结束才能继续执行，
    # 参数如果为0表示等待无限长的事件。
    k = cv2.waitKey(30) & 0xff # 64位机器
    if k == 27: # press 'ESC' to quit
        break

cap.release() # 把摄像头也顺便关了
cv2.destroyAllWindows() # 销毁所有已经创建的窗口
