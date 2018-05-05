import machine
import time
from time import sleep
import ultrasonic
import neopixel
np = neopixel.NeoPixel(machine.Pin(0),8)

trig=machine.Pin(16, machine.Pin.OUT)
echo=machine.Pin(12, machine.Pin.IN)
sensor = ultrasonic.Ultrasonic(trig, echo)


while True:
    distanceFound = sensor.distance()
    print(distanceFound)
    time.sleep(0.2)
    if distanceFound < 0.3:
        np[0] = (50,0,0)
        np.write()
    else:
        np[0] =  (0,0,0)
        np.write()
