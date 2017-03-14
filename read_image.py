import numpy as np
import cv2

# read image in
img = cv2.imread('/Users/scottstubblebine/Desktop/code_hominid_labs/projects/object_recognition/object-classification/dataset/dog-sitting/test/1.jpg', 0)

# name the window being displayed
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# display images
cv2.imshow('image', img)
# display till keystroke
cv2.waitKey(0)
# close window
cv2.destroyAllWindows()
