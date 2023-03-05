import cv2 as cv
import numpy as np 

capture = cv.VideoCapture("OpenCV/Assets/reddetection.mp4")

while True:   
    
    isTrue, frame = capture.read()
    ix, iy = frame.shape[1]//2, frame.shape[0]//2
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    redLower = np.array([140,80,50])
    redUpper = np.array([180,255,255])
    mask = cv.inRange(hsv, redLower, redUpper)
    result = cv.bitwise_and(frame, frame, mask=mask)
    
    gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (13, 13), cv.BORDER_DEFAULT)

    adaptiveThresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
    
    contours, hierarchy = cv.findContours(adaptiveThresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for c in contours:
        (x,y), radius = cv.minEnclosingCircle(c)
        center = (int(x),int(y))
        radius =int(radius)
    
    distance = ((center[0]-ix)**2 + (center[1]-iy)**2)**1/2 
    frame = cv.putText(frame, "Distance:{}".format(distance), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("q"):
        break
capture.release()
cv.destroyAllWindows()




    

    

