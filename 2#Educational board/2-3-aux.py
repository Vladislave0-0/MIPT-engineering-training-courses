import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setmode(GPIO.BCM)
GPIO.setup(aux, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))

GPIO.output(leds, 0)
GPIO.cleanup()