import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

def adc():
    for i in range(256):
        dac_val = dec2bin(i)
        GPIO.output(dac, dac_val)
        comp_val = GPIO.input(comp)
        sleep(0.01)
        if comp_val:
            return i
    return 0

try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256.0
        if i: print("{:.2f)V".format(voltage))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
