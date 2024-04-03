import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    i = 255
    val = 0
    while i > 1:
        GPIO.output(dac, decimal2binary(val + i)[0:8])
        sleep(0.01)
        if GPIO.input(comp) == GPIO.LOW:
            val += i
        i //= 2
    return(val)

try:
    while True:
        vall = adc()
        ll = [1]*((vall // 32)) + [0]*((8 - vall // 32))
        GPIO.output(dac, ll[0:8])
        sleep(1)
        voltage = vall / 256 * 3.3
        if (voltage > 3.3):
            voltage /= 2
        print(f'{voltage:.2f} V')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    
    GPIO.cleanup()
