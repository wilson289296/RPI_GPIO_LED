import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
for x in range(50):
    GPIO.output(8, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(8, GPIO.LOW)
    sleep(0.05)



