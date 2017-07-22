#!/usr/bin/env python

import piconzero as pz, time
from sys import exit
import time
import hcsr04, time

hcsr04.init()
pz.init()

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('gui.html')

@app.route('/api/stop')
def api():
    pz.stop()


@app.route('/api/sensor/<sensorname>')
def api(sensorname):
    if sensorname == 'distance':
        distance = int(hcsr04.getDistance())
        return "Distance:", distance

@app.route('/api/<direction>/<int:speed>')
def api(direction, angle):
    if speed < 0 or speed > 100:
        return "{'error':'out of range'}"

    if direction == 'forward':
        pz.forward(speed)
        return "moving forward"

    elif direction == 'backward':
        pz.backward(speed)
        return "moving backward"

    return "{'error':'invalid direction'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)
