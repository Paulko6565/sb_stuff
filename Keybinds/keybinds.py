import keyboard
import pygetwindow as gw
import playsound
from time import sleep

toggle = 0


def switch_toggle():
    global toggle

    toggle += 1

    if toggle >= 2:
        toggle = 0

    if toggle == 0:
        playsound.playsound("SB.mp3", False)
    elif toggle == 1:
        playsound.playsound("SR.mp3", False)


def press_key(key):
    keyboard.press(key)
    sleep(0.015)
    keyboard.release(key)
    sleep(0.015)


def ability(mode):
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    for window in windows:
        if mode == "others":
            if window.title == "Roblox" and window != previous_focused_window:
                try:
                    window.activate()
                    sleep(0.01)
                    press_key("e")
                except gw.PyGetWindowException:
                    print("Failed to load the window")
        elif mode == "all":
            if window.title == "Roblox":
                try:
                    window.activate()
                    sleep(0.01)
                    press_key("e")
                except gw.PyGetWindowException:
                    print("Failed to load the window")

    if previous_focused_window:
        previous_focused_window.activate()


def reset():
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    for window in windows:
        if window.title == "Roblox" and window != previous_focused_window:
            try:
                window.activate()
                sleep(0.01)
                press_key("esc")
                press_key("r")
                press_key("enter")
            except gw.PyGetWindowException:
                print("Failed to load the window")

    if previous_focused_window:
        previous_focused_window.activate()


def accept():
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    for window in windows:
        if window.title == "Roblox":
            try:
                window.activate()
                sleep(0.01)
                press_key("f1")
            except gw.PyGetWindowException:
                print("Failed to load the window")

    if previous_focused_window:
        previous_focused_window.activate()


def decline():
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    for window in windows:
        if window.title == "Roblox":
            try:
                window.activate()
                sleep(0.01)
                press_key("f2")
            except gw.PyGetWindowException:
                print("Failed to load the window")

    if previous_focused_window:
        previous_focused_window.activate()


def disconnect():
    windows = gw.getAllWindows()

    previous_focused_window = gw.getActiveWindow()

    for window in windows:
        if window.title == "Roblox" and window != previous_focused_window:
            window.close()
            sleep(0.02)
            window.close()

    if previous_focused_window:
        previous_focused_window.activate()


def action(key):
    if key.name == "f6":
        switch_toggle()

    if toggle == 0:  # Slap Battles Mode
        if key.name == "f3":  # uses the ability on every alt except the one you're currently controlling
            ability("others")

        elif key.name == "f4":  # uses the ability on every alt
            ability("all")

        elif key.name == "f5":  # resets every alt except the one you're currently controlling
            reset()

    elif toggle == 1:  # Slap Royale Mode
        if key.name == "f3":  # makes every alt accept the ongoing vote kick
            accept()

        elif key.name == "f4":  # makes every alt decline the ongoing vote kick
            decline()

        elif key.name == "f5":  # makes every alt you're not currently controlling leave the game (the combat logging system will still grant the kill to whoever slapped your alt last)
            disconnect()


keyboard.on_press(action)

keyboard.wait()
