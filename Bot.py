from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#region=(660,350,600,400) this is where game starts from FOR ME may differ
    # im playing in full windows mode
#rgb value of center = (255, 219, 195)

# to stop bot press q
while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(660,350,600,400))

    width, height = pic.size

    for x in range(0,width,5): #(start,finish,increment)
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y)) # this saves the rgb values of pixel located in x,y

            if b == 195: # only doing an exact number because we know color of center in this case will not change
                # for cases w/o same color throughout we can use range (ex: if(b in range(180,210)):)
                click(x+660, y+350) # our region starts at (660,350) hence why we adding those
                time.sleep(0.05) # small delay to make things smoother
                break
