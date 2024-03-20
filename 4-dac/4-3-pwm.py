import RPi.GPIO as GPIO

PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

n = 10
p = GPIO.PWM(PIN, 1000)
p.start(0)

try:
    while True:
        f = int(input())
        p.ChangeDutyCycle(f)
        print(3.3 * f / 100)

finally:
    p.stop()
    GPIO.output(PIN, 0)
    GPIO.cleanup()
