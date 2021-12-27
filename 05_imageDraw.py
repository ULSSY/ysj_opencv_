import cv2
import numpy as np

image=cv2.imread('data/images/mark.jpg')

cv2.imshow('img',image)

#선그리기
imageLine=image.copy()
cv2.line(imageLine,(350,200), (400,183),(0,0,255),3,cv2.LINE_AA)
#cv2.line(imageLine,(350,200), (400,183),(123,23,444),3,cv2.LINE_AA)

cv2.imshow('image Line',imageLine)

#원그리기

cv2.waitkey(0)
cv2.destroyAllWindows()