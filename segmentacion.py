
import numpy as np
import cv2
from matplotlib import pyplot as plt



img = cv2.imread('barnis.jpg')
r=200.0/img.shape[1]
dim=(200,int(img.shape[0]*r))
res= cv2.resize(img,dim, interpolation=cv2.INTER_AREA)

grayscaled = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()




    