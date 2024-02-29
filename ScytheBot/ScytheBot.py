from time import sleep
import keyboard
import pydirectinput
import pyautogui

start_flag = False


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
        click(731, 956)

    elif index == 2:
        click(881, 962)

    elif index == 3:
        click(1035, 962)

    elif index == 4:
        click(1187, 961)

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

def start(key):
    global start_flag
    if key.name == 'q':
        start_flag = True


print("Press 'q' when you're ready to start the bot")
keyboard.on_press(start)

sleep(1)

while True:
    if not start_flag:
        sleep(1)
        pass
    else:
        break


move(500, 500)

#move
hold_key("a", 1)
hold_key("w", 1)

#place a scarecrow
place_troop(1, 731, 521)

#place a farmer1 next to the scarecrow
place_troop(2, 751, 521)

close()

#set the farmer's priority to first
click(751, 521)
priority("First")


#move
hold_key("a", 1)

#wait for money
sleep(6)

#place a scarecrow
place_troop(1, 526, 631)

#wait for money
sleep(7)

#i think you get the drill by now
place_troop(2, 636, 631)

close()

click(636, 631)
priority("First")

sleep(6)

click(636, 631)
buy_upgrade()

sleep(1)

click(526, 631)
buy_upgrade()
close()

hold_key("d", 1)

sleep(5)

click(731, 521)
buy_upgrade()
close()

hold_key("s", 1)

sleep(24)

place_troop(3, 1264, 537)

click(1264, 537)
priority("First")

sleep(16)

place_troop(3, 1349, 531)

click(1349, 531)
priority("First")

hold_key("s", 1)

sleep(9)

place_troop(3, 1312, 574)

click(1312, 574)
priority("Last")

sleep(11)

place_troop(3, 1373, 570)

click(1373, 570)
priority("Last")

hold_key("w", 1)

sleep(14)

click(1264, 537)
buy_upgrade()
close()

sleep(10)

click(1349, 531)
buy_upgrade()
close()
