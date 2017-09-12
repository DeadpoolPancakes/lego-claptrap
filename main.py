import sys
import time
import piconzero as pz
import secondistance as sd
import hcsr04, time

hcsr04.init()
pz.init()
sd.init()

filename = "log.txt"
file = open(filename,"r+")
left = 0
right = 0

try:
    while True:
        distance = int(hcsr04.getDistance())
        rdistance = int(sd.getDistance())
        while distance > 30:
            pz.setMotor(0,-100)
            pz.setMotor(1, 100)
            distance = int(hcsr04.getDistance())
            file.write("forward")
            print ("Distance:", distance)
            print ("weeeeeeeee")
            time.sleep(0.1)
        else:
            print ("uhoh")
            i = 0
            pz.stop()
            rdistance = int(sd.getDistance())
            time.sleep(0.5)
            print ("backing up")
            #back up
            while rdistance > 30 and i < 5: 
                rdistance = int(sd.getDistance())
                file.write("backward")
                pz.setMotor(0,100)
                pz.setMotor(1,-100)
                i = i + 1
                time.sleep(0.1)
            else:    
                print ("looking for new route")
                i = 0
                #rotate left and check distance
                pz.setMotor(0,-100)
                pz.setMotor(1, -100)
                time.sleep(1)
                distanceleft = int(hcsr04.getDistance())
                print ("Distance left:", distanceleft)
                #rotate right and check distance
                pz.setMotor(0,100)
                pz.setMotor(1, 100)
                time.sleep(2)
                distanceright = int(hcsr04.getDistance())
                print ("Distance right:", distanceright)
                if distanceright <= distanceleft:
                    print ("going left")
                    file.write("left /n")
                    pz.setMotor(0,-100)
                    pz.setMotor(1, -100)
                    time.sleep(2)
                    distance = int(hcsr04.getDistance())
                    left = left + 1
                elif left > 0:
                    print ("going left")
                    pz.setMotor(0,-100)
                    pz.setMotor(1, -100)
                    time.sleep(2)
                    file.write("left /n")
                    distance = int(hcsr04.getDistance())
                    right = right + 1
                else:
                    print ("going right")
                    pz.setMotor(1,-100)
                    pz.setMotor(0, -100)
                    time.sleep(2)
                    file.write("right /n")
                    distance = int(hcsr04.getDistance())
                    right = right + 1
except KeyboardInterrupt:
    print ("exiting")
finally:
    hcsr04.cleanup()
    pz.cleanup()