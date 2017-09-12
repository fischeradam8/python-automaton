import autopy
import time


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
    color = autopy.screen.get_color(950, 325)
    print color


def main(rounds):
    time.sleep(5)
    for x in range(0, rounds):
        move_middle()
        clicker(10)
        move_sidebar()
        clicker(5)
        # buy_monster()


main(20)
