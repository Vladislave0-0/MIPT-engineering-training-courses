import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def dectobin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc():
    level = 0
    for i in range(bits - 1, -1, -1):
        level += 2**i
        GPIO.output(dac, dectobin(level))
        time.sleep(0.01)
        comp_val  = GPIO.input(comp)
        if (comp_val == 0):
            level -= 2**i
    return level

def num2_dac_leds(value):
    signal = dectobin(value)
    GPIO.output(dac, signal)
    return signal

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17
bits = len(dac)
levels = 2 ** bits
maxV = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 0)

data_volts = []
data_times = []

try:
    start_time = time.time()
    val = 0
    while(val < 250):
        val = adc()
        print(" volts - {:3}".format(val / levels * maxV))
        num2_dac_leds(val)
        data_volts.append(val)
        data_times.append(time.time() - start_time)

    GPIO.output(troyka, 1)

    while(val > 64):
        val = adc()
        print(" volts - {:3}".format(val/levels * maxV))
        num2_dac_leds(val)
        data_volts.append(val)
        data_times.append(time.time() - start_time)

    end_time = time.time()

    with open("./settings.txt", "w") as file:
        file.write(str((end_time - start_time) / len(data_volts)))
        file.write(("\n"))
        file.write(str(maxV / 256))

    print(end_time - start_time, " secs\n", len(data_volts) / (end_time - start_time), "\n", maxV / 256)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()

data_times_str = [str(item) for item in data_times]
data_volts_str = [str(item) for item in data_volts]

with open("data.txt", "w") as file:
    file.write("\n".join(data_volts_str))

plt.plot(data_times, data_volts)
plt.show()
