from pyautogui import *
import pyautogui
import win32api, win32con
import time
import keyboard

#Tile 1 Position: X:  575 Y:  600 RGB: (178, 183, 234)
#Tile 2 Position: X:  568 Y:  600 RGB: (159, 164, 231)
#Tile 3 Position: X:  748 Y:  600 RGB: (253,  18,   1)
#Tile 4 Position: X:  826 Y:  600 RGB: (166, 171, 233)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(1)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(338, 401)[0] == 0: #if the RGB value = 0 it means its black
        click(338, 401)
    if pyautogui.pixel(427, 398)[0] == 0:
        click(427, 398)
    if pyautogui.pixel(523, 398)[0] == 0:
        click(523, 398)
    if pyautogui.pixel(618, 391)[0] == 0:
        click(618, 391)
