#!/usr/bin/env python

import pantilthat
from sys import exit
import time

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gui.html')

@app route('/look/<item>')
def look(item):
    if item == 'door':
        pantilthat.pan(0)
        pantilthat.tilt(0)
        time.sleep(1)
        return "viewing door"
    
    elif item == 'workshop'
        pantilthat.pan(90)
        pantilthat.tilt(45)
        time.sleep(1)
        return "viewing workshop"

@app.route('/api/<direction>/<int:angle>')
def api(direction, angle):
    if angle < 0 or angle > 180:
        return "{'error':'out of range'}"

    angle -= 90

    if direction == 'pan':
        pantilthat.pan(angle)
        return "{{'pan':{}}}".format(angle)

    elif direction == 'tilt':
        pantilthat.tilt(angle)
        return "{{'tilt':{}}}".format(angle)

    return "{'error':'invalid direction'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)

