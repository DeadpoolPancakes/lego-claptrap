import sys
import time
import piconzero as pz

pz.init()
pz.forward(50)
time.sleep(3)
pz.stop()
time.sleep(1)
pz.spinleft(50)
time.sleep(1)
pz.spinright(50)
time.sleep(1)
pz.revers(50)
time.slee(3)
pz.stop()
pz.cleanup()