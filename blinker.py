import RPi.GPIO as GPIO
import time 

pin = 8

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

try:
	while 1:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(0.25)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.25)
except KeyboardInterrupt:
	GPIO.cleanup()
