import sys
import time
import piconzero as pz
import hcsr04, time

hcsr04.init()
pz.init()
distance = int(hcsr04.getDistance())
try:
    while distance < 10:
        pz.forward(50)
    else:
        pz.stop()    

except KeyboardInterrupt:
    print
finally:
    hcsr04.cleanup()
    pz.cleanup()