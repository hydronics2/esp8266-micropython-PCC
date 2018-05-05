import machine
#dir(machine)   #shows what options are available
led2 = machine.Pin(2, machine.Pin.OUT)
led2.on()
led2.off()

from time import sleep
while True:
    led2.off()
    sleep(0.5)
    led2.on()
    sleep(0.5)
