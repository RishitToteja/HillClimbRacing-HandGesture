import cv2
import os
import time
import HandTrackingModule as htm
import pyautogui
import pydirectinput



# GAS = Point(x=716, y=748)
# BREAK = Point(x=116, y=714)


wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

myList = os.listdir("Images")
pTime = 0
overlayList = []

for img_pth in myList:
    temp = "Images/" + img_pth
    image = cv2.imread(temp)
    image = cv2.resize(image, (200, 200))
    overlayList.append(image)

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw = True)

    if len(lmList) != 0:
        if lmList[8][2] < lmList[6][2]:
            img[0:200, 0:200] = overlayList[0]

            pydirectinput.keyUp('left')
            pydirectinput.keyDown('right')




        else:
            img[0:200, 0:200] = overlayList[1]
            pydirectinput.keyUp('right')
            pydirectinput.keyDown('left')





    cTime = time.time()
    fps = pow((cTime-pTime), -1)
    pTime = cTime

    cv2.imshow("Image", img)
    cv2.waitKey(1)
