import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.IN)

# i = 1000

while True:
    GPIO.output(22, GPIO.input(27))
