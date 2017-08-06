import sys
import time
import piconzero as pz
import secondistance

secondistance.init()
pz.init()


try:    
    while True:
        distance = int(secondistance.getDistance())
        print ("Distance:", distance)
        time.sleep(1)

except KeyboardInterrupt:
    print ("exiting")
finally:
    secondistance.cleanup()
      