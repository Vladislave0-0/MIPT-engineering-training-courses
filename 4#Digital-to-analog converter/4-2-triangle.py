import RPi.GPIO as GPIO
from time import sleep
from funcs import dec2bin
from matplotlib import pyplot as plt
import numpy as np

GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

inc_flag = 1
t = 0 
x = 0

try:
    period = float(input("Type a period for sygnal: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if   x == 0:    inc_flag = 1
        elif x == 255:  inc_flag = 0

        x = x + 1 if inc_flag == 1 else x - 1

        sleep(period/512)
        t += 1

except ValueError:
    print("Inapropriate period!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
    