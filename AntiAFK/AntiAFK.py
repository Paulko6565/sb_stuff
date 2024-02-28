import pydirectinput
import keyboard
import pyautogui
import pygetwindow as gw
from time import sleep

def pressKey(key):
    keyboard.press(key)
    sleep(0.015)
    keyboard.release(key)
    sleep(0.015)

def reset():
    pressKey("esc")
    pressKey("r")
    pressKey("enter")


def action():
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    sleep(0.1)

    for window in windows:
        if window.title == "Roblox":
            try:
                window.activate()
                sleep(0.1)
                pressKey("1")
            except gw.PyGetWindowException:
                pass

    if previous_focused_window:
        previous_focused_window.activate()
for i in range(1, 6):
    sleep(100 * 6)
    action()
    print("10 minutes have passed")
    
print("an hour passed")