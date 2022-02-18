#import webbrowser

# webbrowser.open("https://elearning.wsldp.com/python3/python-open-web-browser/")


#import pyautogui
#import keyboard

# stopKey = "s"  # The stopKey is the button to press to stop. you can also do a shortcut like ctrl+s
# maxX, maxY = pyautogui.size()  # get max size of screen
# while True:
#    if keyboard.is_pressed(stopKey):
#        break

import keyboard
from pynput.mouse import Listener


def is_clicked(x, y, button, pressed):
    for i in range(150):
        keyboard.release.keys(i)


with Listener(on_click=is_clicked) as listener:
    listener.join()


while True:
    if keyboard.read_key() == "p":
        for i in range(150):
            keyboard.block_key(i)
    if keyboard.read_key() == "q":
        print('q')
