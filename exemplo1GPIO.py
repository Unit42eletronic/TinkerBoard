#Electronic assembly using TK board and UNIT 42 board
#	TK GND --- A
#	A --- 1 
#	TK 16 --- 12
#           11 --- 2



import ASUS.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
while 1:
            GPIO.output(16, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(16, GPIO.LOW)
            time.sleep(1)
