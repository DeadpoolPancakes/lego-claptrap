#======================================================================
#
# Python Module to handle an HC-SR04 Ultrasonic Module on a single Pin
# Aimed at use on Picon Zero
#
# Created by Gareth Davies, Mar 2016
# Copyright 4tronix
#
# This code is in the public domain and may be freely copied and used
# No warranty is provided or implied
#
#======================================================================

import RPi.GPIO as GPIO, sys, threading, time, os, subprocess

# Define Sonar Pin (Uses same pin for both Ping and Echo)
trigger = 18
rec = 22

#======================================================================
# General Functions
#
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

def cleanup():
    GPIO.cleanup()
    
def testme():
    return True
#======================================================================

#======================================================================
# UltraSonic Functions
#
# getDistance(). Returns the distance in cm to the nearest reflecting object. 0 == no object
def getDistance():
    GPIO.setup(18, GPIO.OUT)
    # Send 10us pulse to trigger
    GPIO.output(18, True)
    time.sleep(0.00001)
    GPIO.output(18, False)
    start = time.time()
    count=time.time()
    GPIO.setup(22,GPIO.IN)
    while GPIO.input(22)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    while GPIO.input(22)==1 and time.time()-count<0.1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000
    # That was the distance there and back so halve the value
    distance = distance / 2
    return distance

# End of UltraSonic Functions    
#======================================================================

