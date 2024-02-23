from time import sleep
import keyboard
import win32api, win32con
import pydirectinput
import pyautogui

exit_flag = False

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
    keyboard.press(key)
    sleep(0.01)
    keyboard.release(key)


def abort(key):
    global exit_flag
    if key.name == 'q':
        print("Exiting program...")
        exit_flag = True


print("Press 'q' to exit the program.")
keyboard.on_press(abort)

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

    pyautogui.moveTo(width / 2, (height / 2) + -90)

    if scanForColor(whole_screen, 255, 1, 1):
        mouse_pos = pyautogui.position()

        if pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] == 255 and not pyautogui.pixel(mouse_pos[0], mouse_pos[1])[1] == 255:
            print("the portal is right behind the player")
            pressKey("space")
            holdKey("w", 1)

        elif pyautogui.pixel(mouse_pos[0], mouse_pos[1])[2] == 255 and not pyautogui.pixel(mouse_pos[0], mouse_pos[1])[1] == 255:
            print("the default-only portal is behind the player, moving to the left")
            pressKey("space")
            holdKey("a", 0.4)
            pressKey("space")
            holdKey("w", 1)

        elif pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (30, 10, 50), tolerance=80) or pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (130, 130, 130), tolerance=99) or pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] <= 250:
            print("the portal is a little away from behind the player")
            pressKey("space")
            holdKey("a", 0.2)
            pressKey("space")
            holdKey("w", 1)

        else:
            print("i dunno, resetting...")
            abilityAndReset()


def changeCameraAngle():
    #checking if the portal is behind the player

    pixel = pyautogui.screenshot(region=(990, 115, 2, 2))

    if pyautogui.pixel(990, 115)[0] < 200:
        print("the portal is behind the player")

        #rotate the camera around

        pydirectinput.mouseDown(0, 0, "right")
        pydirectinput.move(20, 0)
        pydirectinput.mouseUp(0, 0, "right")

    elif pyautogui.pixel(1279, 252)[2] > 200:
        print("the portal is somewhere to the left of the player")

        #rotate the camera around

        pydirectinput.mouseDown(0, 0, "right")
        pydirectinput.move(-10, 0)
        pydirectinput.mouseUp(0, 0, "right")
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
    sleep(4.5)


sleep(3)

whole_screen = pyautogui.screenshot()

width = whole_screen.width
height = whole_screen.height

#resetting and adjusting the camera
holdKey("i", 1)
holdKey("o", 0.052)
pyautogui.moveTo(width / 2, (height / 2) + -90)
abilityAndReset()


while not exit_flag:
    changeCameraAngle()
    walk()
    abilityAndReset()
    pass
    

