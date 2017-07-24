import sys
import time
import piconzero as pz
import hcsr04, time

hcsr04.init()
pz.init()

try:
    while True:
        distance = int(hcsr04.getDistance())
        while distance > 25:
            pz.setMotor(0,-100)
            pz.setMotor(1, 100)
            distance = int(hcsr04.getDistance())
            print "Distance:", distance
            print "weeeeeeeee"
            time.sleep(0.1)
        else:
            print "uhoh"
            pz.stop()
            time.sleep(0.5)
            print "backing up"
            pz.setMotor(0,75)
            pz.setMotor(1,-75)
            time.sleep(0.5)
            print "looking for new route"
            pz.setMotor(0,-100)
            pz.setMotor(1,-100)
            time.sleep(0.5)
except KeyboardInterrupt:
    print
finally:
    hcsr04.cleanup()
    pz.cleanup()