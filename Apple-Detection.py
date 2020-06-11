import cv2
import numpy as np
import time

# Tracking

def nothing(x):
    pass

# Green Apples
'''cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 22, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 92, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)'''
x = 0
  

while (x<30):
    apples = cv2.imread('Pictures/'+str(x)+'.png')
    hsv_img = cv2.cvtColor(apples, cv2.COLOR_BGR2HSV)

    # Green Mask
    lower1 = np.array([0, 22, 0], dtype="uint8")
    upper1 = np.array([121, 255, 255], dtype="uint8")
    hsv_mask1 = cv2.inRange(hsv_img, lower1, upper1)

    # Red Mask
    lower2 = np.array([0, 22, 55], dtype="uint8")
    upper2 = np.array([92, 255, 255], dtype="uint8")
    hsv_mask2 = cv2.inRange(hsv_img, lower2, upper2)

    # Invert mask 2 colours
    hsv_mask2 = cv2.bitwise_not(hsv_mask2)
    # Combine Green + Red Mask
    combineMask = hsv_mask1 + hsv_mask2
    result = cv2.bitwise_and(apples, apples, mask=combineMask)
    img = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

    # Filter apply
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gblur = cv2.GaussianBlur(gray,(5,5),0)
    blur = cv2.medianBlur(gblur, 5)



    # Circle detecting
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT,1,120,param1=30,param2=25,minRadius=72, maxRadius=96)
    circles = np.uint16(np.around(circles))
    count = 0

    for i in circles[0,:]:
        cv2.circle(apples,(i[0],i[1]),i[2],(0,255,0),6)
        cv2.circle(apples, (i[0], i[1]), 2, (0, 0, 255), 2)
        count +=1

    # Apple counting
    print ("This image contains", count, "apples")
    cv2.imshow("apples", apples)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    x += 1







