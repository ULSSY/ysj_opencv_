import cv2
import numpy as np

from utils import get_four_points

image =cv2.imread('data/images/book1.jpg')

# cv2.imshow('original',image)

point_src=get_four_points(image)
print(point_src)

#변환할 비어있는 이미지를 먼저 하나 만든다.
dst_size=(300,400,3) 

image_dst=np.zeros(dst_size,np.uint8)

#이제, 아까했던 14번 파일처럼!
#이미지는 2개 다 준비됐다
#14번 파일을 참고하여, 실습1번 문제를 해결하세요

#힌트,image의 4개의 점은 마우스클릭으로 해결완료!
#1.image_dst의 4개의 점은 여러분들이 구해서 
point_dst=np.array([0,0,300,0,300,400,0,400])
point_dst=point_dst.reshape(4,2)
#2.행렬 구하고
matrix,status=cv2.findHomography(point_src,point_dst)


#3.변환함수를 통해 ,이미지를 가져오세요.
# 새로운 이미지의 사이즈는 x=400,y=300
#파라미터 셋팅해서 이미지 가져오세요
image_dst=cv2.warpPerspective(image,matrix,(300,400))
cv2.imshow('dst',image_dst)
# #원본 이미지의 4개의 점의 좌표!

# point_original=np.array([141,131,480,159,493,630,64,601],dtype=float)
# point_original=point_original.reshape(4,2)

# print(point_original)

# #다른 이미지 불러와서 , 
# #위의 원본 이미지 4개의 점의 좌표와 매칭되는 점의 좌표도 셋팅
# image_dst=cv2.imread('data/images/book1.jpg')

# cv2.imshow('dst',image_dst)
# point_dst=np.array([318,256,534,372,316,670,73,473],dtype=float)

# point_dst=point_dst.reshape(4,2)
# print(point_dst)

# # #두 이미지의 서로 매칭되는 4개의점이 있으니깐
# # # 이 점들의 정보를 가지고 행렬을 구할 수 있다.
# # matrix,status=cv2.findHomography(point_original,point_dst)

# # #행렬을 구했으면 이미지를 처리할 수 있다.
# # result=cv2.warpPerspective(image,matrix,(image.shape[1],image.shape[0]))

# # cv2.imshow('Warp',result)



cv2.waitKey(0)
cv2.destroyAllWindows()