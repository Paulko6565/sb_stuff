import pydirectinput
import keyboard
import pygetwindow as gw
from time import sleep

def pressKey(key):
    keyboard.press(key)
    sleep(0.01)
    keyboard.release(key)
    sleep(0.01)

def reset():
    pressKey("esc")
    pressKey("r")
    pressKey("enter")

def iterate_through_windows(window_title, action):
    # Get all windows
    windows = gw.getAllWindows()

    # Remember the previously focused window
    previous_focused_window = gw.getActiveWindow()

    # Loop through each window
    for window in windows:
        # Check if the window title exactly matches the specified title
        if window.title == window_title:
            window.activate()

            if action == "reset":
                reset()

    # Return to the previously focused window
    if previous_focused_window:
        previous_focused_window.activate()

# Replace "Your Window Title" with the exact title of the windows you want to target
window_title = "Roblox"

iterate_through_windows(window_title, "reset")
