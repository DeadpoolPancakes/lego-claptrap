import sys
import time
import piconzero as pz
import hcsr04, time

hcsr04.init()
pz.init()
distance = int(hcsr04.getDistance())
while distance > 10:
    pz.forward(50)
else    
    while distance < 10
        pz.backward(10)
        if distance > 10
            pz.stop()
            sleep.time(1)
            pz.spinLeft(50)
            time.sleep(2)
            pz.stop() 

except KeyboardInterrupt:
    print
finally:
    hcsr04.cleanup()
    pz.cleanup()