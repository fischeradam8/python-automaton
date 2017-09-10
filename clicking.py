import autopy
import time


def capsing():
    autopy.key.toggle(autopy.key.MOD_META, True)
    time.sleep(1)
    autopy.key.tap('1')
    # for x in range(0, 5):
        #


def alerter():
    autopy.alert.alert('Helloka!')


def clicker():
    time.sleep(5)
    for x in range (0, 10):
        autopy.mouse.click(autopy.mouse.LEFT_BUTTON)
        time.sleep(1)


clicker()
