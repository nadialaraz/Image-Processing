import cv2
import numpy as np

img = cv2.imread('image\kucingbelang.jpg',0)

# Deteksi Garis Lurus
minLineLength = 60
maxLineGap = 40
threshold = 20

# Deteksi Lingkaran
dp = 1
minDist = 50
param1 = 40
param2 = 30
minRadius = 0
maxRadius = 0

img_eq = img
# Normalisasi citra
img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

# Histogram equalization
img_eq = cv2.equalizeHist(img_norm)

# Transformasi Hough

# Deteksi Garis Lurus 
# lines = cv2.HoughLinesP(img_eq,1,np.pi/180,threshold,minLineLength,maxLineGap)
# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv2.line(img_eq,(x1,y1),(x2,y2),(255,0,0),2)

# cv2.imshow('Deteksi Garis',img_eq)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Deteksi Lingkaran
# circles = cv2.HoughCircles(img_eq,cv2.HOUGH_GRADIENT,dp,minDist,
#                             param1=param1,param2=param2,
#                             minRadius=minRadius,maxRadius=maxRadius)
# if circles is not None:
#     circles = np.round(circles[0,:]).astype(int)
#     for (x,y,r) in circles:
#         cv2.circle(img_eq,(x,y),r,(0,255,0),2)

# cv2.imshow('Deteksi Lingkaran',img_eq)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Deteksi Sembarang
lines = cv2.HoughLines(img_eq,1,np.pi/180,threshold)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img_eq,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Deteksi Sembarang',img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()