import sys
import time
import piconzero as pz
import secondistance as sd
import hcsr04, time
#import sensors as sens
#import vlc

hcsr04.init()
pz.init()
sd.init()
#sens.init()

filename = "log.txt"
file = open(filename,"r+")
left = 0
right = 0
f = 0
speed = 50

try:
    while True:
        distance = int(hcsr04.getDistance())
        rdistance = int(sd.getDistance())
        while distance > 25:
            f = f + 1
            pz.forward(speed)
            distance = int(hcsr04.getDistance())
            if f == 100:
                print ("Distance:", distance)
                print ("weeeeeeeee")
                file.write("forward\n")
                #p = vlc.MediaPlayer("file:///home/pi/music/claptrap.py")
                #p.play()
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
            while rdistance > 30 and i < 25: 
                rdistance = int(sd.getDistance())
                file.write("backward\n")
                pz.reverse(speed)
                i = i + 1
                time.sleep(0.01)
            else:    
                print ("looking for new route")
                i = 0
                #rotate left and check distance
                pz.spinLeft(speed)
                time.sleep(0.5)
                distanceleft = int(hcsr04.getDistance())
                time.sleep(0.1)
                print ("Distance left:", distanceleft)
                #rotate right and check distance
                pz.spinRight(speed)
                time.sleep(1)
                distanceright = int(hcsr04.getDistance())
                time.sleep(0.1)
                print ("Distance right:", distanceright)
                # if stuck in a loop of left right actions this should break it out of it
                if left >= 5 and right >= 5:
                    print ("getting out of corner")
                    pz.spinLeft(speed)
                    time.sleep(2)
                    right = 0
                    left = 0
                elif distanceright <= distanceleft:
                    print ("going left")
                    file.write("left\n")
                    pz.spinLeft(speed)
                    time.sleep(1)
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