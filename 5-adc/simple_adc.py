import RPi.GPIO as GPIO
from time import sleep

def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

def adc():
    for i in range(256):
        dac_val = decimal2binary(i)
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
        if i: 
            print(f'{voltage:.2f} V')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
