import RPi.GPIO as GPIO
from time import sleep

def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
led = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

def adc(troyka):
    k = 0
    for i in range (7, -1, -1):
        k += 2**i
        GPIO.output(dac, decimal2binary(k))
        sleep(0.01)
        comp_input = GPIO.input(comp)
        if(comp_input == 1):
            k -= 2**i 
    return k


try:
    while(True):
        k=0
        t=0
        c=0
        while(c<adc(troyka)):
            k += 2**t
            t += 1
            c += 32
        GPIO.output(led, decimal2binary(k))
        print(f'{3.3 * adc(troyka) / 255:.2f} V')
finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.cleanup()
