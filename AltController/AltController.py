import pydirectinput
import keyboard
import pygetwindow
import pygetwindow as gw
import pyautogui
import random
from time import sleep

pyautogui.useImageNotFoundException()

whole_screen = pyautogui.screenshot()

width = whole_screen.width
height = whole_screen.height

def scroll(direction):
    pyautogui.scroll(direction)

def pressKey(key):
    keyboard.press(key)
    sleep(0.015)
    keyboard.release(key)
    sleep(0.015)

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

def useAbility():
    gloveArea = pyautogui.screenshot(region=(925, 1000, 100, 100))
    gloveEquipped = scanForColor(gloveArea, 90, 142, 233)

    if gloveEquipped:
        print("the user has their glove equipped")
        pressKey("e")
    else:
        pressKey("1")
        pressKey("e")

def dance():
    gloveArea = pyautogui.screenshot(region=(925, 1000, 100, 100))
    gloveEquipped = scanForColor(gloveArea, 90, 142, 233)

    if gloveEquipped:
        pressKey("1")

    pressKey("/")
    chat("e dance")

def changeCameraAngle():
    gloveArea = pyautogui.screenshot(region=(925, 1000, 100, 100))
    gloveEquipped = scanForColor(gloveArea, 90, 142, 233)

    if gloveEquipped:
        return

    holdKey("i", 1)
    for i in range(1, 7):
        scroll(-150)
        sleep(0.1)

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
    gloveArea = pyautogui.screenshot(region=(925, 1000, 100, 100))
    gloveEquipped = scanForColor(gloveArea, 90, 142, 233)

    if gloveEquipped:
        return
    
    whole_screen = pyautogui.screenshot()
    pyautogui.moveTo(width / 2, (height / 2) + -90)

    mouse_pos = pyautogui.position()

    if pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (255, 255, 255)):
        reset()

    elif pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (159, 213, 218), tolerance=80):
        reset()

    elif pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] == 255 and not pyautogui.pixel(mouse_pos[0], mouse_pos[1])[1] == 255:
        pressKey("space")
        holdKey("w", 1)

    elif pyautogui.pixel(mouse_pos[0], mouse_pos[1])[2] == 255 and not pyautogui.pixel(mouse_pos[0], mouse_pos[1])[1] == 255:
        pressKey("space")
        holdKey("a", 0.4)
        pressKey("space")
        holdKey("w", 1)

    elif pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1], (30, 10, 50), tolerance=80) or pyautogui.pixelMatchesColor(mouse_pos[0], mouse_pos[1],(130, 130, 130), tolerance=99) or pyautogui.pixel(mouse_pos[0], mouse_pos[1])[0] <= 250:
        pressKey("space")
        holdKey("a", 0.2)
        sleep(0.2)
        pressKey("space")
        holdKey("w", 1)

    else:
        reset()

def scatter():
    pydirectinput.mouseDown(0, 0, "right")
    pydirectinput.move(0, 100)
    pydirectinput.mouseUp(0, 0, "right")

    sleep(0.1)

    scroll(-10000)

    pyautogui.moveTo(width / 2 + random.randint(-300, 300), height / 2 + random.randint(-300, 300))
    pydirectinput.click(0, 0, 1, 0, "right")

def tournament():
    gloveArea = pyautogui.screenshot(region=(925, 1000, 100, 100))
    gloveEquipped = scanForColor(gloveArea, 90, 142, 233)

    if gloveEquipped:
        pressKey("1")

    try:
        button = pyautogui.locateCenterOnScreen("accept.png", confidence=0.8)
        pydirectinput.click(button.x, button.y)
        sleep(0.1)

    except pyautogui.ImageNotFoundException:
        return

def switchWindow():
    windows = gw.getWindowsWithTitle("Roblox")

    for window in windows:
        if window.title == "Roblox Account Manager":
            windows.pop(windows.index(window))

    randomWindow = random.randint(0, len(windows) - 1)

    try:
        windows[randomWindow].activate()
    except pygetwindow.PyGetWindowException as e:
        print("error", e)
        pass

def checkChat():
    chatMessage = pyautogui.screenshot(region=(0, 254, 400, 25))
    chatMessage.save(r"C:\Users\Admin\Desktop\AltController\chat.png")
    
    #reset command
    try:
        resetCommand = pyautogui.locateOnScreen("reset.png", grayscale=True, confidence=0.935, region=(0, 254, 400, 25))
        if resetCommand:
            chat("respawning...")
            action("reset")
    except pyautogui.ImageNotFoundException:
        pass

    #arena command
    try:
        arenaCommand = pyautogui.locateOnScreen("arena.png", grayscale=True, confidence=0.935, region=(0, 254, 400, 25))
        if arenaCommand:
            chat("entering the arena...")
            action("ability")
            action("jump")
            action("camera")
            action("arena")
    except pyautogui.ImageNotFoundException:
        pass

    #dance command
    try:
        danceCommand = pyautogui.locateOnScreen("dance.png", grayscale=True, confidence=0.95, region=(0, 254, 400, 25))
        if danceCommand:
            chat("initiating epik moves")
            action("dance")
    except pyautogui.ImageNotFoundException:
        pass

    #jump command
    try:
        jumpCommand = pyautogui.locateOnScreen("jump.png", grayscale=True, confidence=0.935, region=(0, 254, 400, 25))
        if jumpCommand:
            chat("hop")
            action("jump")
    except pyautogui.ImageNotFoundException:
        pass

    #ability command
    try:
        abilityCommand = pyautogui.locateOnScreen("ability.png", grayscale=True, confidence=0.935, region=(0, 254, 400, 25))
        if abilityCommand:
            chat("using gloves...")
            action("ability")
    except pyautogui.ImageNotFoundException:
        pass

    #scatter command
    try:
        scatterCommand = pyautogui.locateOnScreen("scatter.png", grayscale=True, confidence=0.934, region=(0, 254, 400, 25))
        if scatterCommand:
            chat("walking to a random position...")
            action("scatter")
    except pyautogui.ImageNotFoundException:
        pass

    #slap command
    try:
        slapCommand = pyautogui.locateOnScreen("slap.png", grayscale=True, confidence=0.934, region=(0, 254, 400, 25))
        if slapCommand:
            chat("bonk")
            action("slap")
    except pyautogui.ImageNotFoundException:
        pass

    #tournament command
    try:
        tournamentCommand = pyautogui.locateOnScreen("tournament.png", grayscale=True, confidence=0.934, region=(0, 254, 400, 25))
        if tournamentCommand:
            chat("attempting to join the competition...")
            action("tournament")
    except pyautogui.ImageNotFoundException:
        pass
def action(action, argument=None):
    windows = gw.getAllWindows()
    
    previous_focused_window = gw.getActiveWindow()
    
    for window in windows:
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
            elif action == "ability":
                useAbility()
            elif action == "scatter":
                scatter()
            elif action == "slap":
                pydirectinput.click()
                sleep(0.09)
            elif action == "tournament":
                tournament()
            else:
                print("Error")
                return
    
    if previous_focused_window:
        previous_focused_window.activate()


sleep(1)

windowSwitchTimer = 8

while True:
    checkChat()
    sleep(0.2)
