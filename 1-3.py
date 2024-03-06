import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_IN = 23
GPIO_OUT = 26
GPIO.setup(GPIO_IN, GPIO.IN)
GPIO.setup(GPIO_OUT, GPIO.OUT)

input = GPIO.input(GPIO_IN)
if input:
    GPIO.output(GPIO_OUT, 1)
    time.sleep(10)
print(input)

GPIO.cleanup()
