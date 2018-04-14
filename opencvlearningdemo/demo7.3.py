import cv2
import numpy as np

img = cv2.imread('1.jpg')
img2  = cv2.imread('2c.jpg')

rows,cols,channels = img2.shape
roi = img[0:rows, 0:cols]

GrayImage=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)  

# 中值滤波  
GrayImage= cv2.medianBlur(GrayImage,5)  

# mask_bin 是黑白掩膜
ret,mask_bin  = cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)  

#mask_inv 是反色黑白掩膜
mask_inv = cv2.bitwise_not(mask)

# 黑白掩膜 和 大图切割区域 取和
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_bin)

#反色黑白掩膜 和 logo 取和
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)

dst = cv2.add(img1_bg,img2_fg) 
img[0:rows, 0:cols ] = dst

cv2.imshow('GrayImage',mask_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()




