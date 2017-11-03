import RPi.GPIO as GPIO, sys, threading, time, os, subprocess
from gpiozero import LightSensor, Buzzer, LED

lights = LED(12)
ldr = LightSensor(14)



def init():
    GPIO.setup(lights,GPIO.OUT)

def setlights(self, state):
    if state == 'on':
        lights.on() 
    else:
        lights.off()   
def getLightLevel(self):
   return ldr.value