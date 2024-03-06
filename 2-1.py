import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)

NUM_CYCLES = 3
PAUSE      = 0.2

for i in range(NUM_CYCLES):
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(PAUSE)
        GPIO.output(led, 0)

GPIO.cleanup()
