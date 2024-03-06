import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def showNumber(number):
    for i in range(dac.__len__()):
        GPIO.output(dac[dac.__len__() - i - 1], (number & (1 << i)) >> i)

numbers = [255, 127, 64, 32, 5, 0, 256]
for n in numbers:
    showNumber(n)


GPIO.output(dac, 0)
GPIO.cleanup()

plt.figure(figsize = (7, 4))
U = [3253, 1673, 866, 456, 74, 0, 0]
plt.scatter(numbers, U)
plt.show()
