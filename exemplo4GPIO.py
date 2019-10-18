import RPi.GPIO as GPIO
from time import sleep

pin=input("Enter Pin:")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)


x=1
while 1:
                white=GPIO.PWM(pin,x)
               
                sleep(3)
                
                white.stop()
                x=x+100
     
