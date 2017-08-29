import sys
import time
import piconzero as pz
import secondistance as sd
import hcsr04, time

hcsr04.init()
pz.init()

debug = True

try:
    while True:
        distance = int(hcsr04.getDistance())
        rdistance = int(sd.getDistance())
        while distance > 20:
            pz.setMotor(0,-100)
            pz.setMotor(1, 100)
            distance = int(hcsr04.getDistance())
            if debug = true:
                print ("Distance:", distance)
                print ("weeeeeeeee")
            time.sleep(0.1)
        else:
            print ("uhoh")
            i = 0
            pz.stop()
            rdistance = int(sd.getDistance())
            time.sleep(0.5)
            if debug = true:
                print ("backing up")
            #back up
            while rdistance > 20 or i < 5: 
                rdistance = int(sd.getDistance())
                pz.setMotor(0,100)
                pz.setMotor(1,-100)
                i = i + 1
                time.sleep(0.1)
            else
            if debug = true:    
                print ("looking for new route")
            i = 0
            #rotate left and check distance
            pz.setMotor(0,-100)
            pz.setMotor(1, -100)
            time.sleep(0.5)
            distanceleft = int(hcsr04.getDistance())
            if debug = true:
                print ("Distance left:", distanceleft)
            #rotate right and check distance
            pz.setMotor(0,100)
            pz.setMotor(1, 100)
            time.sleep(1)
            distanceright = int(hcsr04.getDistance())
            if debug = true:
                print ("Distance right:", distanceright)
            if distanceright < distanceleft:
                if debug = true:
                    print ("going left")
                pz.setMotor(0,-100)
                pz.setMotor(1, -100)
                time.sleep(1)
                distance = int(hcsr04.getDistance())
            else:
                if debug = true:
                    print ("going right")
                distance = int(hcsr04.getDistance())

except KeyboardInterrupt:
    print ("exiting")
finally:
    hcsr04.cleanup()
    pz.cleanup()