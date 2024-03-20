import RPi.GPIO as GPIO
import dec2bin

MAX_VOLTAGE = 3.3

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        N = input('Enter a number in range [0, 256): ')
        try:
            N = int(N)
            if 0 <= N < 256:
                GPIO.output(dac, dec2bin.decimal2binary(N))
                voltage = float(N) / 256 * MAX_VOLTAGE
                print(f'Output voltage: {voltage: .4f}')
            else:
                print('Number is out of range, try again')
        except Exception:
            if N == 'q':
                break
            print('Invalid input format, try again')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
