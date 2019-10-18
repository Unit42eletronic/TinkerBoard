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
