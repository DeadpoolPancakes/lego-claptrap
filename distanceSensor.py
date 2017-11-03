#======================================================================
# modified from 4tronix picon zero hcsr04 library to accept two ints get distancs.
# this was done to use multiple hcsr04 sensors on the board
#======================================================================

import RPi.GPIO as GPIO, sys, threading, time, os, subprocess

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def cleanup():
    GPIO.cleanup()


def getDistance(trigger, receiver):
    GPIO.setup(trigger, GPIO.OUT)

    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    start = time.time()
    count=time.time()
    GPIO.setup(receiver,GPIO.IN)
    while GPIO.input(receiver)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    while GPIO.input(receiver)==1 and time.time()-count<0.1:
        stop = time.time()
    elapsed = stop-start
    distance = elapsed * 34000
    distance = distance / 2
    return distance
