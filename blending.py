import cv2
import numpy as np

# must change sizes of images to be the same
img1 = cv2.resize(cv2.imread('images/ml.png'),(100,100))
img2 = cv2.resize(cv2.imread('images/opencv-logo.png'),(100,100))

# blend
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

# display image
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
