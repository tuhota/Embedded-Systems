import RPi.GPIO as GPIO
import time 

#define pin for output
pin = 8

#set pin numbering
GPIO.setmode(GPIO.BOARD)

#set pin to output mode
GPIO.setup(pin, GPIO.OUT)

try:
	while 1:
		#turn on pin, wait, turn off, wait, to create blink effect
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(0.25)
		GPIO.output(pin, GPIO.LOW)
		time.sleep(0.25)
	#thrown on interrupt signal
except KeyboardInterrupt:
	#reset pins to input mode
	GPIO.cleanup()
