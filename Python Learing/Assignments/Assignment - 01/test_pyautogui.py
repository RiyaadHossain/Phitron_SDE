import pyautogui
import time 


n = int(input())
time.sleep(2)

for i in range(1,n+1):
    for j in range(1, i+1):
        pyautogui.write("#")
    pyautogui.press('enter')
