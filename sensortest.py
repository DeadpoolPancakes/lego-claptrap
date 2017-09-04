import sys
import time
import distanceSensor as ds

ds.init()


try:    
    while True:
        distanceone = int(ds.getDistance(12,15))
        distancetwo = int(ds.getDistance(38, 38))
        print ("Distance One:", distanceone)
        print ("Distance Two:", distancetwo)
        time.sleep(1)

except KeyboardInterrupt:
    print ("exiting")
finally:
    ds.cleanup()
      