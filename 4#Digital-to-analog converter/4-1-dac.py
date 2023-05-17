import RPi.GPIO as GPIO
import funcs

GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Type a number from 0 to 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, funcs.dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"Output voltage is about {voltage:.4} volt")
            else:
                if num < 0:
                    print("Number have to be >=0! Try again...")
                elif num > 255:
                    print("Number is out of range [0,255]! Try again...")  
        except Exception:
            if num == "q": break
            print("You have to type a number, not string! Try again...")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
    