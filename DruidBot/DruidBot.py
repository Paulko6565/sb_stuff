from time import sleep, time
import keyboard
import pydirectinput
import pyautogui


def move(x, y):
    pyautogui.moveTo(x, y)

    pydirectinput.move(0, 1)
    sleep(0.05)

def click(x, y):
    move(x, y)

    pydirectinput.mouseDown(None, None)
    sleep(0.05)
    pydirectinput.mouseUp(None, None)


def hold_key(key, duration):
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)


def close():
    click(663, 479)

def place_troop(index, x, y):
    if index == 1:
        click(813, 980)

    elif index == 2:
        click(959, 962)

    click(x, y)


def priority(mode):
    if mode == "First":
        click(547, 751)

    elif mode == "Last":
        click(547, 751)
        click(547, 751)

    elif mode == "Strongest":
        click(547, 751)
        click(547, 751)
        click(547, 751)

    close()


def buy_upgrade():
    click(212, 746)


print("Press 'q' when you're ready to start the bot")
keyboard.wait("q")

move(500, 500)

hold_key("w", 2)
hold_key("a", 0.5)

place_troop(1, 524, 666)

sleep(2)

click(524, 666)
priority("First")

place_troop(1, 604, 654)

click(604, 654)
priority("First")

sleep(13)

place_troop(1, 684, 647)

click(684, 647)
priority("First")

sleep(55)

place_troop(1, 508, 712)

click(508, 712)
priority("Last")

place_troop(1, 590, 706)

click(590, 706)
priority("Last")

sleep(5)

place_troop(1, 674, 700)

click(674, 700)
priority("Last")

sleep(5)

hold_key("s", 1)

place_troop(2, 276, 1007)

click(276, 1007)
priority("First")

sleep(5)

place_troop(2, 488, 1001)

click(488, 1001)
priority("First")

sleep(2)

place_troop(2, 665, 997)

click(665, 997)
priority("First")

sleep(10)

click(276, 1007)
buy_upgrade()

sleep(2)

click(488, 1001)
buy_upgrade()

sleep(4)

click(665, 997)
buy_upgrade()

sleep(15)

click(276, 1007)
buy_upgrade()

sleep(4)

click(488, 1001)
buy_upgrade()

sleep(25)

click(665, 997)
buy_upgrade()