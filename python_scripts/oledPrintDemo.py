import machine, ssd1306
import time
from time import sleep

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

print(i2c.scan()) #print any i2c devices available

oled.fill(0)
oled.text('this is a test', 0,0)
oled.text('..on the ESP8266', 0,20)
oled.text('what to do now?', 0,40)
oled.show()
