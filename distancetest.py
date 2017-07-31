import sys
import time
import piconzero as pz
import hcsr04, time

hcsr04.init()
pz.init()

try:
    while True:
        distance = int(hcsr04.getDistance())
        while distance > 20:
            pz.setMotor(0,-100)
            pz.setMotor(1, 100)
            distance = int(hcsr04.getDistance())
            print ("Distance:", distance)
            print ("weeeeeeeee")
            time.sleep(0.1)
        else:
            print ("uhoh")
            pz.stop()
            time.sleep(0.5)
            print ("backing up")
            #back up
            pz.setMotor(0,75)
            pz.setMotor(1,-75)
            time.sleep(0.3)
            print ("looking for new route")
            #rotate left and check distance
            pz.setMotor(0,-75)
            pz.setMotor(1, -75)
            time.sleep(0.5)
            distanceleft = int(hcsr04.getDistance())
            #rotate right and check distance
            pz.setMotor(0,75)
            pz.setMotor(1, 75)
            time.sleep(1)
            distanceright = int(hcsr04.getDistance())
            if distanceleft < distanceright:
                print ("going left")
                pz.setMotor(0,-75)
                pz.setMotor(1, -75)
                time.sleep(1)
                distance = int(hcsr04.getDistance())
            else:
                print ("going right")
                distance = int(hcsr04.getDistance())

except KeyboardInterrupt:
    print ("exiting")
finally:
    hcsr04.cleanup()
    pz.cleanup()