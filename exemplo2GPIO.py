#Electronic assembly using TK board and UNIT 42 board
#	TK GND --- A
#	A --- 1 
#	A --- 3
#	A --- 5
#	TK 11 --- 16
#           TK 12 --- 14
#	TK 13 --- 12
#	15 --- 6
#	13 --- 4
#           11 --- 2

import ASUS.GPIO as GPIO
import time
verde=11
amarelo=12
vermelho=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(amarelo, GPIO.OUT)
GPIO.setup(vermelho, GPIO.OUT)
while 1:
            GPIO.output(vermelho, GPIO.LOW)
            GPIO.output(verde, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(verde, GPIO.LOW)
            GPIO.output(amarelo, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(amarelo, GPIO.LOW)
            GPIO.output(vermelho, GPIO.HIGH)
            time.sleep(4)
