import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils

imgpath = "A:\\opencv projects\\Document Scanner\\r.jpg"
img = cv2.imread(imgpath)
print(img.shape)
ratio = img.shape[0] / 500.0
h = 500
w = 500
sh = (h,w)
new_img = cv2.resize(img, sh, interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
canny = cv2.Canny(gray, 80, 200)

contour, heirarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#contour = imutils.grab_contours(contour)
#contour = sorted(contour,key = cv2.contourArea(), reverse = True)[:5]
l = []
#for c in contour:
#    l.append((c[0],c[1]))

print(l)
print(len(l))
    

for cnt in contour:
    approx = cv2.approxPolyDP(cnt, 0.02* cv2.arcLength(cnt, True), True)
    (x,y,h,w) = cv2.boundingRect(cnt)
    #print(cnt)
    
    
    if((len(approx)==4) and (cv2.contourArea(cnt)>100)):#it will be a rectamgle
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)
        
pts = []
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)

#for proper perspective
points1 = np.float32([[114,203] , [326,192], [142,555], [379,524]])
points2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])        

#save_path = "A:\\opencv projects\\Document Scanner" 

cv2.imshow('edges',canny)
#cv2.imwrite(save_path, canny)
cv2.imshow('img',img)
#cv2.imwrite(save_path,img)

cv2.setMouseCallback('img', click_event)

cv2.imshow('new',new_img)
#cv2.imwrite(save_path,new_img)
#matrix = cv2.getPerspectiveTransform(points1,points2)
#result = cv2.warpPerspective(img, matrix, (700,720))
result_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(result_gray, 156, 246,cv2.THRESH_BINARY)
#cv2.imshow('transformed', result)
cv2.imshow('final',thresh)
#cv2.imwrite(save_path, thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

