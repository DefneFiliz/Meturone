import cv2 as cv
import numpy as np 

class Editor():

    def __init__(self):
        self.image = cv.imread("OpenCV/Assets/image.jpg")
        self.drawingRect = False
        self.drawingRing = False
        self.ix, self.iy = -1, -1

    def resize(self):
        imageResized = cv.resize(self.image, (800,800))
        self.image = imageResized
    
    def events(self, event, x, y, flags, param):        
        #ROTATE
        if event == cv.EVENT_RBUTTONDOWN and not (flags & cv.EVENT_FLAG_CTRLKEY or flags & cv.EVENT_FLAG_ALTKEY):
            imageRotated = cv.rotate(self.image, cv.ROTATE_90_CLOCKWISE)
            self.image = imageRotated
        elif event == cv.EVENT_LBUTTONDOWN and not (flags & cv.EVENT_FLAG_CTRLKEY or flags & cv.EVENT_FLAG_ALTKEY):
            imageRotated = cv.rotate(self.image, cv.ROTATE_90_COUNTERCLOCKWISE)
            self.image = imageRotated
        #RECTANGLE
        elif event == cv.EVENT_LBUTTONDOWN and flags & cv.EVENT_FLAG_CTRLKEY:
            self.drawingRect = True
            self.ix, self.iy = x, y
        elif event == cv.EVENT_MOUSEMOVE and self.drawingRect and flags & cv.EVENT_FLAG_CTRLKEY:
            cv.rectangle(self.image, (self.ix, self.iy), (x, y), (255, 255, 255), 2)
        elif event == cv.EVENT_LBUTTONUP and flags & cv.EVENT_FLAG_CTRLKEY:
            self.drawingRect = False
            crop = self.image[min(self.ix, x):max(self.ix, x), min(self.iy, y):max(self.iy, y)]
            cv.imwrite("cropped.jpg", crop)
        #TEXT
        if event == cv.EVENT_LBUTTONDOWN and flags & cv.EVENT_FLAG_ALTKEY:
            font = cv.FONT_HERSHEY_SIMPLEX
            org = (x, y)
            color = (int(self.image[org][0]), int(self.image[org][1]), int(self.image[org][2]))   
            updated = cv.putText(self.image, "Defne", org, font, 1, color, 2, cv.LINE_AA)
            self.image = updated
        #RING
        if event == cv.EVENT_RBUTTONDOWN and flags & cv.EVENT_FLAG_CTRLKEY:
            self.drawingRing = True
            self.ix, self.iy = x, y
        elif event == cv.EVENT_MOUSEMOVE  and flags & cv.EVENT_FLAG_CTRLKEY and self.drawingRing:
            radius = int(((self.ix-x)**2 + (self.iy-y)**2) ** (1/2))
            updated = cv.circle(self.image, (self.ix, self.iy), radius, (255, 255, 255), 2)
            self.image = updated
        elif event == cv.EVENT_RBUTTONUP and flags & cv.EVENT_FLAG_CTRLKEY:
            self.drawingRing = False
        #SAVE
        if event == cv.EVENT_RBUTTONDOWN and flags & cv.EVENT_FLAG_ALTKEY:
            cv.imwrite("img.jpg", self.image)

    def runner(self):
        cv.namedWindow("Editor")
        cv.setMouseCallback("Editor", self.events)
        while True:
            cv.imshow("Editor", self.image)
            if cv.waitKey(1) & 0XFF==ord("q"):
                break
        cv.destroyAllWindows()

Editor().resize()
Editor().runner()


        