import autopy
import time
import math
import random


def capsing():
    autopy.key.toggle(autopy.key.MOD_META, True)
    time.sleep(1)
    autopy.key.tap('1')
    # for x in range(0, 5):
        #


def alerter(text):
    autopy.alert.alert(text)


def move_middle():
    autopy.mouse.move(500, 500)


def move_sidebar():
    autopy.mouse.move(950, 325)


def clicker(number):
    for x in range(0, number):
        autopy.mouse.click(autopy.mouse.LEFT_BUTTON)
        time.sleep(0.1)


def buy_monster():
    level_up = autopy.bitmap.Bitmap.open('screens/level_up.png')
    pos = autopy.bitmap.capture_screen().find_bitmap(level_up)
    if pos is None:
        print('Continuing')
    else:
        autopy.mouse.move(pos[0]+25, pos[1]+25)
        time.sleep(0.2)
        clicker(2)


def collect():
    for x in range(300):
        autopy.mouse.move(500, 500+x)
        time.sleep(0.0001)


def main(rounds):
    time.sleep(5)
    for x in range(0, rounds):
        move_middle()
        clicker(10)
        # move_sidebar()
        clicker(5)
        buy_monster()


# main(100)

time.sleep(0.5)
collect()

# todo: lescrollozni, utána körbenézni, majd visszascrollozni, kell még fel/le nyíl és buy screenshot