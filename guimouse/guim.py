import pyautogui
import htm as htn
import time
import numpy as np
import cv2
from tkinter import *
from PIL import ImageTk, Image
import sys

root = Tk()
flag = False


def exit():
    if cv2.waitKey(1) & flag == True:
        cv2.release()
        cv2.destroyAllWindows()
        sys.exit(0)


def mouse():
    #################
    wCam, hCam = 640, 480
    pTime = 0
    cTime = 0
    detector = htn.handDetector(maxHands=1)
    wScr, hScr = pyautogui.size()
    frameR = 100  # frame reduction
    smoothering = 4
    plocX, plocY = 0, 0
    clocx, clocy = 0, 0  # current location x e y
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    #################
    while True:
        # 1 finf hands landmarks
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        # 2. find the index finger and the middle finger
        if len(lmList) != 0:
            # print(lmList)
            # posizione ell'indice e del medio
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            # 3. check what fingers are up
            fingers = detector.fingersUp()
            # 4. only inderx finger: moving mode

            cv2.rectangle(img, (frameR, frameR),
                          (wCam-frameR, hCam-frameR), (255, 0, 255), 2)

            if fingers[1] and fingers[2] == False:
                # 5. convert coordinates

                x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
                # 6. smoothen values
                clocx = plocX + (x3-plocX) / smoothering
                clocy = plocY + (y3-plocY) / smoothering
                # 7. move mouse
                pyautogui.moveTo(wScr-clocx, clocy)
                cv2.circle(img, (x1, y1), 50, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocx, clocy
        # 8. both index and middle fingers are up: clicking mode
            elif fingers[1] and fingers[2]:
                # 9. find distance beetween fingers
                length, img, infoLine = detector.findDistance(8, 12, img)
                # 10. Click mouse if distance is short
                if length < 30:
                    cv2.circle(img, (infoLine[4], infoLine[5]),
                               15, (0, 255, 0), cv2.FILLED)
                    pyautogui.click()

        # 11. frame rate
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 58),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        # 12. display
        cv2.imshow("image", img)

        cv2.waitKey(1)


# si pu?? aggiungere uno state state=DISABLED
# padx la larghezza
# pady l'altezza
# fg per il colore del testo
# bg per il colore sfondo
myButton = Button(root, text="Attiva Mouse", padx=50, pady=10,
                  command=mouse, fg="blue", bg="green")
myButtonExit = Button(root, text="Spegni", padx=50,
                      pady=10, command=exit, fg="blue", bg="red")

myButton.pack()
myButtonExit.pack()

cv2.waitKey(0)
cv2.destroyAllWindows()
root.mainloop()
