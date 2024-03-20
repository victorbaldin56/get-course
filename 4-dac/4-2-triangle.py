import RPi.GPIO as GPIO
import dec2bin
import time

MAX_VOLTAGE = 3.3

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    period = float(input())
    inc_flag = 0
    N = 0 
    while True:
        GPIO.output(dac, dec2bin.decimal2binary(N))
        voltage = float(N) / 256 * MAX_VOLTAGE
        print(f'Output voltage: {voltage: .4f}')

        if N == 0:
            inc_flag = 1
        elif N == 255:
            inc_flag = -1
        
        N += inc_flag
        time.sleep(period / 512)

except ValueError:
    print('Invalid input format')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
