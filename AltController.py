import pydirectinput
import keyboard
import pygetwindow as gw
import pyautogui
from time import sleep

whole_screen = pyautogui.screenshot()

width = whole_screen.width
height = whole_screen.height

def pressKey(key):
    keyboard.press(key)
    sleep(0.02)
    keyboard.release(key)
    sleep(0.02)

def holdKey(key, duration):
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def chat(sentence):
    pressKey("/")
    for i in sentence:
        pressKey(i)

    pressKey("enter")

def scanForColor(screenshot, findR, findG, findB):
    width, height = screenshot.size

    done = False

    for x in range(0, width, 5):
        if done:
            break

        for y in range(0, height, 5):
            r, g, b = screenshot.getpixel((x, y))

            if findR == r and findG == g and findB == b:
                return [x, y]

def reset():
    pressKey("esc")
    pressKey("r")
    pressKey("enter")

def dance():
    pressKey("/")
    chat("e dance")

def changeCameraAngle():
    if pyautogui.pixelMatchesColor(959, 1003, (90, 142, 233), tolerance=90):
        return

    holdKey("i", 1)
    holdKey("o", 0.3)

    if pyautogui.pixel(990, 115)[0] < 200:
        pydirectinput.mouseDown(0, 0, "right")
        pydirectinput.move(20, 0)
        pydirectinput.mouseUp(0, 0, "right")

    elif pyautogui.pixel(1279, 252)[2] > 200:
        pydirectinput.mouseDown(0, 0, "right")
        pydirectinput.move(-10, 0)
        pydirectinput.mouseUp(0, 0, "right")
    else:
        reset()
        return

def walkToArena():
    whole_screen = pyautogui.screenshot()
    pyautogui.moveTo(width / 2, (height / 2) + -90)

    mouse_pos = pyautogui.position()

    if pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] == 255 and not pyautogui.pixel(mouse_pos[0], mouse_pos[1])[
                                                                         1] == 255:
        print("the portal is right behind the player")
        pressKey("space")
        holdKey("w", 1)

    elif pyautogui.pixel(mouse_pos[0], mouse_pos[1])[2] == 255 and not pyautogui.pixel(mouse_pos[0], mouse_pos[1])[
                                                                           1] == 255:
        print("the default-only portal is behind the player, moving to the left")
        pressKey("space")
        holdKey("a", 0.4)
        pressKey("space")
        holdKey("w", 1)

    elif pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (30, 10, 50),
                                     tolerance=80) or pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1],
                                                                                  (130, 130, 130), tolerance=99) or \
            pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] <= 250:
        print("the portal is a little away from behind the player")
        pressKey("space")
        holdKey("a", 0.2)
        pressKey("space")
        holdKey("w", 1)

    else:
        print("i dunno, resetting...")
        reset()


def action(action, argument=None):
    # Get all windows
    windows = gw.getAllWindows()

    # Remember the previously focused window
    previous_focused_window = gw.getActiveWindow()

    # Loop through each window
    for window in windows:
        # Check if the window title exactly matches the specified title
        if window.title == "Roblox":
            window.activate()

            if action == "reset":
                reset()
            elif action == "camera":
                changeCameraAngle()
            elif action == "arena":
                walkToArena()
            elif action == "jump":
                pressKey("space")
            elif action == "dance":
                dance()
            elif action == "chat" and argument:
                chat(argument)
            elif action == "disconnect":
                window.close()
                sleep(0.05)
                window.close()
                sleep(0.05)
            else:
                print("Error")
                return


    # Return to the previously focused window
    if previous_focused_window:
        previous_focused_window.activate()

action("reset")

sleep(5)

action("disconnect")