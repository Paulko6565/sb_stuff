import keyboard
import pygetwindow as gw
from time import sleep

def pressKey(key):
    keyboard.press(key)
    sleep(0.015)
    keyboard.release(key)
    sleep(0.015)


def action(key):
    if key.name == "f1": #uses the ability on every alt except the one you're currently controlling
        windows = gw.getAllWindows()

        previous_focused_window = gw.getActiveWindow()

        for window in windows:
            if window.title == "Roblox" and window != previous_focused_window:
                try:
                    window.activate()
                    sleep(0.01)
                    pressKey("e")
                except gw.PyGetWindowException:
                    window.activate()
                    sleep(0.01)
                    pressKey("e")

        if previous_focused_window:
            previous_focused_window.activate()

    elif key.name == "f2": #uses the ability on every alt
        windows = gw.getAllWindows()

        previous_focused_window = gw.getActiveWindow()

        for window in windows:
            if window.title == "Roblox":
                try:
                    window.activate()
                    sleep(0.01)
                    pressKey("e")
                except gw.PyGetWindowException:
                    window.activate()
                    sleep(0.01)
                    pressKey("e")

        if previous_focused_window:
            previous_focused_window.activate()

    elif key.name == "f3": #resets every alt except the one you're currently controlling
        windows = gw.getAllWindows()

        previous_focused_window = gw.getActiveWindow()

        for window in windows:
            if window.title == "Roblox" and window != previous_focused_window:
                try:
                    window.activate()

                    sleep(0.01)

                    pressKey("esc")
                    pressKey("r")
                    pressKey("enter")
                except gw.PyGetWindowException:
                    window.activate()

                    sleep(0.01)

                    pressKey("esc")
                    pressKey("r")
                    pressKey("enter")

        if previous_focused_window:
            previous_focused_window.activate()


keyboard.on_press(action)

keyboard.wait("f4")
