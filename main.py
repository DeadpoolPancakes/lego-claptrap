import sys
import time
import piconzero as pz
import secondistance as sd
import hcsr04, time
import sensors as sens

hcsr04.init()
pz.init()
sd.init()
sens.init()

filename = "log.txt"
file = open(filename,"r+")
left = 0
right = 0
f = 0



try:
    while True:
        distance = int(hcsr04.getDistance())
        rdistance = int(sd.getDistance())
        while distance > 25:
            f = f + 1
            pz.setMotor(0,-100)
            pz.setMotor(1, 100)
            distance = int(hcsr04.getDistance())
            if f == 100:
                print ("Distance:", distance)
                print ("weeeeeeeee")
                file.write("forward\n")
                f = 0
            time.sleep(0.01)
        else:
            print ("uhoh")
            i = 0
            pz.stop()
            rdistance = int(sd.getDistance())
            time.sleep(0.5)
            print ("backing up")
            #back up
            while rdistance > 30 and i < 50: 
                rdistance = int(sd.getDistance())
                file.write("backward\n")
                pz.setMotor(0,100)
                pz.setMotor(1,-100)
                i = i + 1
                time.sleep(0.01)
            else:    
                print ("looking for new route")
                i = 0
                #rotate left and check distance
                pz.setMotor(0,-100)
                pz.setMotor(1, -100)
                time.sleep(1)
                distanceleft = int(hcsr04.getDistance())
                time.sleep(0.1)
                print ("Distance left:", distanceleft)
                #rotate right and check distance
                pz.setMotor(0,100)
                pz.setMotor(1, 100)
                time.sleep(2)
                distanceright = int(hcsr04.getDistance())
                time.sleep(0.1)
                print ("Distance right:", distanceright)
                # if stuck in a loop of left right actions this should break it out of it
                if left >= 5 and right >= 5:
                    print ("getting out of corner")
                    pz.setMotor(0,-100)
                    pz.setMotor(1, -100)
                    time.sleep(5)
                    right = 0
                    left = 0
                elif distanceright <= distanceleft:
                    print ("going left")
                    file.write("left\n")
                    pz.setMotor(0,-100)
                    pz.setMotor(1, -100)
                    time.sleep(2)
                    distance = int(hcsr04.getDistance())
                    left = left + 1
                else:
                    print ("going right")
                    file.write("right\n")
                    distance = int(hcsr04.getDistance())
                    right = right + 1
except KeyboardInterrupt:
    print ("exiting")
finally:
    hcsr04.cleanup()
    pz.cleanup()