from time import sleep
import keyboard
import random
import win32api, win32con
import pydirectinput
import pyautogui

def click(x,y, button):
    win32api.SetCursorPos((x,y))

    if button == "left":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    if button == "right":
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def holdKey(key, duration):
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

def pressKey(key):
    keyboard.press_and_release(key)


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

def walk():
    whole_screen = pyautogui.screenshot()

    if scanForColor(whole_screen, 255, 1, 1):
        mouse_pos = pyautogui.position()

        if pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] == 255:
            print("the portal is right behind the player")
            holdKey("w", 1)
            abilityAndReset()

        elif pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (30, 10, 50), tolerance=80) or pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (130, 130, 130), tolerance=99) or pyautogui.pixel(mouse_pos[0], mouse_pos[1])[1] == 255 or pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] <= 250:
            print("the portal is a little away from behind the player")
            holdKey("a", 0.2)
            holdKey("w", 1)
            abilityAndReset()

        elif pyautogui.pixel(mouse_pos[0], mouse_pos[1])[2] == 255:
            print("the default-only portal is behind the player, moving to the left")
            holdKey("a", 0.4)
            holdKey("w", 1)
            abilityAndReset()

        else:
            print("i dunno, resetting...")
            abilityAndReset()

def changeCameraAngle():
    #checking if the portal is behind the player

    pixel = pyautogui.screenshot(region=(990, 115, 2, 2))
    pixel.save(r"C:\Users\Admin\PycharmProjects\pythonProject\pixel.png")

    if pyautogui.pixel(990, 115)[0] < 200:
        print("the portal is behind the player")

        #rotate the camera around

        holdKey("right", 1.29)

        walk()

    elif pyautogui.pixel(1279, 252)[2] > 200:
        print("the portal is somewhere to the left of the player")

        #rotate the camera around

        holdKey("left", 0.58)

        walk()

    else:
        print("i dunno, resetting...")
        abilityAndReset()

def abilityAndReset():
    pressKey("e")
    sleep(0.01)
    pressKey("esc")
    sleep(0.01)
    pressKey("r")
    sleep(0.01)
    pressKey("enter")

sleep(1)

whole_screen = pyautogui.screenshot()

width = whole_screen.width
height = whole_screen.height

pyautogui.moveTo(width / 2, (height / 2) + -90)

while keyboard.is_pressed('q') == False:
    changeCameraAngle()
    sleep(3.5)