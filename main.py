import pyautogui
import time
from random_qoute import write_in_txt
import random


screenWidth, screenHeight = pyautogui.size()

print("please point the mouse on the target point and press Crtl+C ")

try:
    while True:
        targetMouseX, targetMouseY = pyautogui.position()
        print(targetMouseX, targetMouseY, end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"target Point is {targetMouseX},{targetMouseY}")


# move mouse to target position and click
pyautogui.moveTo(targetMouseX, targetMouseY, duration=1)

pyautogui.click()

write_in_txt("qoutes")
qoutes_set = {x.rstrip() for x in open("qoutes.txt")}
len_qoutes_set = len(qoutes_set)

while True:
    # get a random qoute in list format
    random_qoute = list(qoutes_set)[random.randint(0, len_qoutes_set)]
    random_qoute_list = random_qoute.split(" ")

    for word in random_qoute_list:
        random_interval = random.random()
        pyautogui.write(f"{word} ", interval=random_interval / 3.0)
    pyautogui.hotkey("ctrl", "a", "backspace")
