import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PORT = 26
GPIO.setup(PORT, GPIO.OUT)
while True:
    GPIO.output(PORT, 1)
    time.sleep(1)
    GPIO.output(PORT, 0)
    time.sleep(1)
