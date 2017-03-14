import cv2
import numpy as np

# start timer
e1 = cv2.getTickCount()
# your code execution
# stop timer
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)


img1 = cv2.imread('images/messi5.jpg')
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

# Result I got is 0.521107655 seconds

# make sure that cv2.useOptimized() returns True, else run cv2.setUseOptimized(True|False)
