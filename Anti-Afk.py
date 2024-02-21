import pydirectinput
import pygetwindow as gw
import time

def press_space_in_windows(window_title):
    # Find all windows with the specified title
    windows = gw.getWindowsWithTitle(window_title)

    if len(windows) == 0:
        print("No windows found with the title:", window_title)
        return

    # Remember the previously focused window
    previous_focused_window = gw.getActiveWindow()

    # Loop through each window and press space
    for window in windows:
        print("Pressing space in window:", window.title)
        window.activate()
        # Give some time for the window to come to the foreground
        time.sleep(1)
        # Press space key
        pydirectinput.press('space')

    # Return to the previously focused window
    if previous_focused_window:
        previous_focused_window.activate()

# Replace "Your Window Title" with the title of the windows you want to target
window_title = "Roblox"

while True:
    press_space_in_windows(window_title)
    print("Space pressed in all windows. Waiting for 10 minutes...")
    # Wait for 10 minutes before repeating
    time.sleep(10 * 60)
