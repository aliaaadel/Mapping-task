#!/usr/bin/env python
# coding: utf-8

# In[41]:


import cv2
import matplotlib.pyplot as plt 
import numpy as np
import imutils
import math


# In[83]:


img = cv2.imread('transect.jpg')
img_hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
sharpen = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

bottom = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]]) # for horizontal lines 
#img_hsv = cv2.filter2D(img_hsv, -1, sharpen)
#img_hsv = cv2.filter2D(img_hsv, -1, bottom)
#img_hsv = cv2.Sobel(img_hsv,cv2.CV_64F,0,1,ksize=5)
#img_hsv = cv2.Sobel(img_hsv,cv2.CV_64F,0,1,ksize=5)
L = np.array([0,46,134], dtype=np.uint8)
U=np.array([187,153,214], dtype=np.uint8)
mask = cv2.inRange(img_hsv, L,U)
plt.imshow(mask,cmap='gray')


# In[ ]:





# In[173]:


#getting lines in image 
rho = 1
theta = np.pi/180
threshold = 60
min_line_length = 100
max_line_gap =5
img_copy = np.copy(img)
lines = cv2.HoughLinesP(mask, rho, theta, threshold, np.array([]),min_line_length, max_line_gap)
horizontal = []
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img_copy,(x1,y1),(x2,y2),(255,0,0),5)
        #horizontal lines
        Angle = math.atan2(abs(y2 - y1), abs(x2 - x1)) * 180.0 / np.pi;
        print (Angle)
        if (Angle >= 0 and Angle<=10 ):
            horizontal.append([[x1,y1,x2,y2]])
        
plt.imshow(img_copy)


# In[174]:


img_copy2 = np.copy(img)
for line in horizontal:
    for x1,y1,x2,y2 in line:
        cv2.line(img_copy2,(x1,y1),(x2,y2),(255,0,0),5)
        
plt.imshow(img_copy2)      


# In[216]:


# sort lines and get only 2 lines 
filtered_lines=[]
sort=sorted(horizontal,key=lambda l:l[0][1], reverse=True)
# error in this loop 
for i in range(len(sort)):
    if ((sort[i][0][1] - sort[i-1][0][1]))>20: # compare y in the current line and next one 
        filtered_lines.append(sort[i])
        
        print(True)
    
    


# In[211]:


filtered_lines


# In[214]:


rows = []

y = img.shape[0]
for line in filtered_lines:
    for x1,y1,x2,y2 in line:
        y_avg=(y1+y2)/2
        if (abs(y-y_avg)>100):
            crop= img[int(y):int(y_avg), :]
            rows.append(crop)
            y= y_avg
            print(True)


# In[213]:





# In[ ]:




