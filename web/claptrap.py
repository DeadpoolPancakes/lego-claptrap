#!/usr/bin/env python
from sys import exit
import time
import hcsr04
import piconzero as pz
import secondistance as sd

hcsr04.init()
pz.init()
sd.init()

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('gui.html')


@app.route('/api/stop')
def stop():
    """define the stop endpoint"""
    pz.stop()
    return {"stop"}


@app.route('/api/sensor/<sensorname>')
def sensor(sensorname):
    """define the sensor endpoint"""
    if sensorname == 'distance':
        distance = int(hcsr04.getDistance())
        return {"Distance:", distance}
    if sensorname == 'light':
        lightlevel = int(4)
        return {"light level = ", lightlevel}


@app.route('/api/<direction>')
def direction(direction):
    """define the direction endpoint"""
    speed = 100
    if direction == 'forward':
        distance = int(hcsr04.getDistance())
        if distance > 20:
            pz.forward(speed)
            time.sleep(0.5)
            pz.stop()
            return {"moving forward"}
        else:
            return {"There is something in the way"}

    elif direction == 'backward':
        rdistance = int(sd.getDistance())
        if rdistance > 20
            pz.reverse(speed)
            time.sleep(0.5)
            pz.stop()
            return {"moving backward"}
        else:
            return {"There is something in the way"}

    elif direction == 'left':
        pz.spinLeft(speed)
        time.sleep(0.5)
        pz.stop()
        return {"rotating left"}

    elif direction == 'right':
        pz.spinRight(speed)
        time.sleep(0.5)
        pz.stop()
        return {"rotating right"}

    return "{'error':'invalid direction'}"

@app.route('/api/<action>')
def action(action):
    """define the action endpoint"""
    speed = 100

    if action == 'dance':
        i = 0
        while i < 4:
            pz.forward(speed)
            time.sleep(0.5)
            pz.spinLeft(speed)
            time.sleep(0.2)
            pz.spinRight(speed)
            time.sleep(0.2)
            pz.spinLeft(speed)
            time.sleep(0.2)
            pz.spinRight(speed)
            time.sleep(0.2)
            pz.reverse(speed)
            time.sleep(0.5)
            i = i + 1
            return {"Uhntssuhntssuhntss"}
        return {"I love a good dance"}

    if action == 'twirl':
        pz.spinLeft(speed)
        time.sleep(1.5)
        return{"weeee, oh i feel dizzy now"}

    if action == 'wave':
        return {"hellooooo"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)