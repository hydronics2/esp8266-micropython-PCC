import machine, ssd1306
import time
from time import sleep
import ultrasonic

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

trig=machine.Pin(16, machine.Pin.OUT)
echo=machine.Pin(12, machine.Pin.IN)
sensor = ultrasonic.Ultrasonic(trig, echo)

while True:
    print("top of the loop")
    oled.fill(0)
    distance = sensor.distance()
    print(distance)
    oled.text(str(distance),0,0)
    oled.show()
    time.sleep(0.1)
