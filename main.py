import pyautogui
import time
from random_qoute import random_qoute



screenWidth, screenHeight = pyautogui.size()
#(162,518)
print('please point the mouse on the target point and press Crtl+C ')

try:
    while True:
        targetMouseX, targetMouseY = pyautogui.position()
        print(targetMouseX,targetMouseY,end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f'target Point is {targetMouseX},{targetMouseY}')

#set pause
pyautogui.PAUSE = 2.5

#move mouse to target position and send random text
pyautogui.moveTo(targetMouseX, targetMouseY, duration=1)

#get a random qoute in list format
random_qoute_list = random_qoute().split(' ')




