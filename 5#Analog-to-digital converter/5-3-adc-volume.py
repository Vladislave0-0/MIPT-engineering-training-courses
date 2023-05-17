import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11,  9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        dac_val = dec2bin(k)
        GPIO.output(dac, dac_val)
        sleep(0.01)
        comp_val = GPIO.input(comp)
        if comp_val == 0:
            k -= 2**i
    return k

def Volume(val):
    val = int(val/256*10)
    arr = [0]*8
    for i in range(val - 1):
        arr[i] = 1
    return arr

try:
    while True:
        i = adc()
        if i:
            volume_val = Volume(i)
            GPIO.output(led, volume_val)
            print(int(i/256*10))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")