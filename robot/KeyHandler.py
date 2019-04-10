import threading
import RPi.GPIO as GPIO
import time

key_longtime = 2
key_stop = 0

BUTTON = 12
BUTTON1 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
wukong = None

def start(wk):
    wukong = wk
    t = threading.Thread(target=keyHandler)
    t.start()


def key1Press():
    print("key1short")
    wukong.wake()


def key2Press():
    print("key2short")


def key1LPress():
    print("key1long")


def key2LPress():
    print("key2long")


def keyHandler():
    while True:
        key1 = GPIO.input(BUTTON)
        key2 = GPIO.input(BUTTON1)

        if not key1:
            keep_time = 0
            while not GPIO.input(BUTTON):
                keep_time = keep_time + 1
                time.sleep(1)
            if keep_time >= key_longtime:
                key1LPress()
            else:
                key1Press()

        if not key2:
            keep_time = 0
            while not GPIO.input(BUTTON1):
                keep_time = keep_time + 1
                time.sleep(1)
            if keep_time >= key_longtime:
                key2LPress()
            else:
                key2Press()

        time.sleep(0.1)
