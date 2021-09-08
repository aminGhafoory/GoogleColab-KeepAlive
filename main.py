import pyautogui
import time
from random_qoute import random_qoute
import random


screenWidth, screenHeight = pyautogui.size()

print('please point the mouse on the target point and press Crtl+C ')

try:
    while True:
        targetMouseX, targetMouseY = pyautogui.position()
        print(targetMouseX,targetMouseY,end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f'target Point is {targetMouseX},{targetMouseY}')


#move mouse to target position and click
pyautogui.moveTo(targetMouseX, targetMouseY, duration=1)

pyautogui.click()

while True:
    #get a random qoute in list format
    random_qoute_list = random_qoute().split(' ')
    random_interval = random.random()
    for word in random_qoute_list:
        pyautogui.write(f'{word} ', interval=random_interval/5.)
    pyautogui.hotkey('ctrl', 'a', 'backspace')
    
        



