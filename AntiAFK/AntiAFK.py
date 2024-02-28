import keyboard
import pygetwindow as gw
from time import sleep

def pressKey(key):
    keyboard.press(key)
    sleep(0.015)
    keyboard.release(key)
    sleep(0.015)


def action():
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    sleep(0.1)

    for window in windows:
        if window.title == "Roblox":
            try:
                window.activate()
                sleep(0.1)
                pressKey("1")  # equips / un-equips your glove
            except gw.PyGetWindowException:
                print("the program can't access this roblox window for some reason, woops")

    if previous_focused_window:
        previous_focused_window.activate()


while True:
    action()
    sleep(100 * 6)  # waits for 10 minutes before doing the action again
