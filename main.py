import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
#(162,518)
print('please point the mouse on the target point and press Crtl+C ')

try:
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        print(currentMouseX,currentMouseY,end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f'target Point is{currentMouseX},{currentMouseY}')



