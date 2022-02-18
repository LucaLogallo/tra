import pyautogui
import htm as htn
import time
import numpy as np
import cv2
from tkinter import *
from PIL import ImageTk, Image
import sys
import win32api


root = Tk()


def exit():
    sys.exit(0)


def mouse():
    #################
    wCam, hCam = 640, 480
    pTime = 0
    cTime = 0
    detector = htn.handDetector(maxHands=1)
    wScr, hScr = pyautogui.size()
    frameR = 100  # frame reduction
    frame2r = 300
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
            x1, y1 = lmList[4][1:]
            x2, y2 = lmList[8][1:]
            x3, y3 = lmList[12][1:]
            x4, y4 = lmList[16][1:]
            x5, y5 = lmList[20][1:]
            x6 = np.interp(x1, (frameR, wCam-frame2r), (0, wScr))
            y6 = np.interp(y1, (frameR, hCam-frame2r), (0, hScr))
            x7 = np.interp(x2, (frameR, wCam-frame2r), (0, wScr))
            y7 = np.interp(y2, (frameR, hCam-frame2r), (0, hScr))
            x8 = np.interp(x3, (frameR, wCam-frame2r), (0, wScr))
            y8 = np.interp(y3, (frameR, hCam-frame2r), (0, hScr))
            x9 = np.interp(x4, (frameR, wCam-frame2r), (0, wScr))
            y9 = np.interp(y4, (frameR, hCam-frame2r), (0, hScr))
            x10 = np.interp(x5, (frameR, wCam-frame2r), (0, wScr))
            y10 = np.interp(y5, (frameR, hCam-frame2r), (0, hScr))
            print("x6")
            print(x6)
            print("x7")
            print(x7)
            print("x8")
            print(x8)
            print("x9")
            print(x9)
            print("x10")
            print(x10)
            print("y6")
            print(y6)
            print("y7")
            print(y7)
            print("y8")
            print(y8)
            print("y9")
            print(y9)
            print("y10")
            print(y10)

            cv2.rectangle(img, (frameR, frameR),
                          (wCam-frameR, hCam-frameR), (255, 0, 255), 2)

            cv2.rectangle(img, (frame2r, frame2r),
                          (wCam-frame2r, hCam-frame2r), (255, 0, 0), 3)

            # if (x6 > frame2r or x7 > frame2r or x8 > frame2r or x9 > frame2r or x10 > frame2r) and (y6 > frame2r or y7 > frame2r or y8 > frame2r or y9 > frame2r or y10 > frame2r) or (x6 < wCam-frame2r or x7 < wCam-frame2r or x8 < wCam-frame2r or x9 < wCam-frame2r or x10 < wCam-frame2r) or (y6 < hCam-frame2r or y7 < hCam-frame2r or y8 < hCam-frame2r or y9 < hCam-frame2r or y10 < hCam-frame2r):

            # 6. smoothen values
            #clocx = plocX + (x3-plocX) / smoothering
            #clocy = plocY + (y3-plocY) / smoothering
            #win32api.MessageBox(0, 'hello', 'title')
        # 11. frame rate
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 58),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        # 12. display
        cv2.imshow("image", img)

        cv2.waitKey(1)


# si può aggiungere uno state state=DISABLED
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
