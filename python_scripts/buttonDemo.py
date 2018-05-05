import machine
import time
from time import sleep

import neopixel
np = neopixel.NeoPixel(machine.Pin(0),8)

button = machine.Pin(14, machine.Pin.IN)
#button = machine.Pin(14,machine.Pin,IN, machine.Pin.PULL_UP) #add an input pullup only available on some pins



while True:
    test = button.value()
    print(test)
    time.sleep(0.05)
    if test:
        np[0] = (50,0,0)
        np.write()
    else:
        np[0] =  (0,0,0)
        np.write()
