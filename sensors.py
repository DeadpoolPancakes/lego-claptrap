import RPi.GPIO as GPIO, sys, threading, time, os, subprocess

lights = 12
ldr = 13



def init():
    GPIO.setup(lights,GPIO.OUT)
    GPIO.setup(ldr, GPIO.IN)

def getlights(self, state):
    if state == 'on':
        GPIO.output(lights, True) 
    else:
        GPIO.output(lights, False)    
