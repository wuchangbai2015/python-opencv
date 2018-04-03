import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
cv2.rectangle(img,(350,0),(500,128),(0,255,0),3)#矩形
cv2.circle(img,(425,63),63,(0,0,255),-1)#圆， -1为向内填充
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)#定义frame的大小
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

