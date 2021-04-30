import numpy as np
import cv2 as cv
def drawongrid(row,column,shape,color):
   point=((4*row+2)*33,(4*column+2)*33)
   if(shape=='circle'):
       cv.circle(img,point,40,color,2)
   if(shape=='sqaure'):
       cv.rectangle(img,(point[0]-40,point[1]-40),(point[0]+40,point[1]+40),color,2)
   if(shape=='rectangle'):
       cv.rectangle(img,(point[0]-40,point[1]-20),(point[0]+40,point[1]+20),color,2)
   if(shape=='ellipse'):
       cv.ellipse(img,(point[0]+66,point[1]),(100,50),0,0,360,color,2)




if __name__ == '__main__':
    img=np.zeros([4*99,4*297,3])
# Grid lines at these intervals (in pixels)
# dx and dy can be different
    dx, dy = 4*33,4*33

# Custom (rgb) grid color
    grid_color = [255,0,0]

# Modify the image to include the grid
    img[:,::dy,:] = grid_color
    img[::dx,:,:] = grid_color

# Show the result
    drawongrid(1,2,'ellipse',[255,255,255])
    cv.imshow('a',img)
    cv.waitKey(0)
