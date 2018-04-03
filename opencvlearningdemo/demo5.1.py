import cv2
import numpy
#--我们可以根据像素的行和列的坐标获取它们的像素值
#--对BGR图像而言,返回的是B,G,R的像素值
#--对灰度图像而言,返回的是灰度值
img = cv2.imread('demo1.jpg')#读一个图片

#使用数组下标索引的方式,访问图片的像素
px=img[100,100]
print(px)

bule    = img[100,100,0]  #返回这一点B的分量像素值
print("B pixel value:",bule)
 
green    = img[100,100,1] #返回这一点G的分量像素值
print("G pixel value:",green)
 
red      = img[100,100,2] #返回这一点R的分量像素值
print("R pixel value:",red)

img[101,101]=[255,255,255]
print(img[101,101])






