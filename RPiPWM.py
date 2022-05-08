import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)



#define speed of sound in cm
s_of_s = 34300

#setup pin for led
led = 8
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

#define frequency in Hz
pwm = GPIO.PWM(led, 1000)     
pwm.start(0)

#setup pins for echo and trg
echo = 10
trg = 12
GPIO.setup(echo, GPIO.IN)
GPIO.setup(trg, GPIO.OUT)



def get_dist():
    #power trg  for 0.01ms
    GPIO.output(trg, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trg, GPIO.LOW)
 
    #store time at transmit
    while GPIO.input(echo) == False:
        start = time.time()
 
    #store time at receive
    while GPIO.input(echo) == True:
        stop = time.time()
 
    travel_time = stop - start
    
    #to calculate distance, time of flight is multiplied by speed of sound, 
    #then divided by 2 due to the forward and return journey
    dist = (travel_time * s_of_s) / 2
 
    return dist



while True:
    #gets distance and outputs rounded integer
    dist = get_dist()
    print (str(int(dist)) + "cm")
    
    #to screen invalid data, conditional applied
    if dist <= 10 and dist >= 0:
        #alter led per function of distance, brightness correlates with proximity
        pwm.ChangeDutyCycle((11 - dist) * 10)
    else:
        #else if beyond range or invalid variable, led off
        pwm.ChangeDutyCycle(0)

    time.sleep(0.1)
