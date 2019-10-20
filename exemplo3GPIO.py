#Electronic assembly using TK board and UNIT 42 board
#       TK GND --- A
#	      A --- 1 
#	      TK pin --- 12
#       11 --- 2

import RPi.GPIO as GPIO
from time import sleep

pin=input("Enter Pin:")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
                
pwm = GPIO.PWM(pin, 100)    # Created a PWM object
pwm.start(0)                    # Started PWM at 0% duty cycle
try:
    while 1:                    # Loop will run forever
       for x in range(100):    # This Loop will run 100 times
           pwm.ChangeDutyCycle(x) # Change duty cycle
           sleep(0.01)         # Delay of 10mS
           # If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
    pass        # Go to next line
               
     
