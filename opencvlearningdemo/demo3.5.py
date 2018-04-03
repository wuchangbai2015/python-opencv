import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
#这里reshape的第一个参数为-1， 表明这一维度的长度是根据后面的维度计算出来的
cv2.polylines(img,[pts],True,(0,255,255))
#注意第三个参数若是False， 我们得到的是不闭合的线

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',1000,1000)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



