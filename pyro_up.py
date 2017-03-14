import cv2
import numpy as np
import matplotlib as plt

higher_reso = cv2.imread('images/messi5.jpg')
lower_reso = cv2.pyrDown(higher_reso)

# not the same as higher_reso
higher_reso2 = cv2.pyrUp(lower_reso)

cv2.imshow('lower_reso', higher_reso2)
cv2.waitKey(0)
cv2.destroyAllWindows()
