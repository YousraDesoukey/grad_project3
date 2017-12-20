import cv2
import numpy as np

img = cv2.imread('c6.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 150, 255,0)
canny= cv2.Canny(thresh, 30, 200)
kernel= np.ones((3, 3), np.uint8)
canny= cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel, iterations=5)
cv2.imshow('After canny and closing',canny)
image,contours,hierarchy = cv2.findContours(canny,2,1)
img2 = cv2.drawContours(image , contours, -1, (150,255,0), 3)
cv2.imshow('All Contours',img2)
print(contours)
cnts = sorted(contours, key = cv2.contourArea, reverse=True)[:30]
c = max(contours, key = cv2.contourArea)
print(c)
print(cnts)
print(cv2.contourArea(cnts[0]))


#cnt = contours[1]
#cnt1= cv2.contourArea(cnts[0],int)
for cnt in cnts:
    if ((cv2.contourArea(cnt) < cv2.contourArea(cnts[0])-cv2.contourArea(cnts[0])*0.5)):
        break
    else:
        x,y,w,h = cv2.boundingRect(cnt)
        img3 = cv2.rectangle(img,(x,y),(x+w,y+h),(0,200,150),2)
cv2.imshow('After Segmentation',img3)
cv2.waitKey(0)