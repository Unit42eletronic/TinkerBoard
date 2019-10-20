#Change the color of the RGB in ur board

import ASUS.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.output(3, 0)
GPIO.output(5, 0)
GPIO.output(40, 0)
while 1:
            GPIO.output(3, 1)
            time.sleep(1)
            GPIO.output(3, 0)
            time.sleep(3)
            GPIO.output(5, 1)
            time.sleep(1)
            GPIO.output(5, 0)
            time.sleep(3)
            GPIO.output(40, 1)
            time.sleep(1)
            GPIO.output(40, 0)
            time.sleep(3)
