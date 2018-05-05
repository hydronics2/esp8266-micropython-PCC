import time
import machine
import neopixel
print("here we are")

# initiate with pin number (5) and number of leds (8)
np = neopixel.NeoPixel(machine.Pin(0),8)
n = 8 #enter number of pixels in array
print("starting while loop")
print("exit while loop with ctrl c")
while True:
    # cycle white
    print("swiping white")
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)
    # cycle red
    print("swiping red")
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (128, 0, 0)
        np.write()
        time.sleep_ms(25)

        # bounce
    print("bouncing blue")
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    print("rading red")
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    print("clearing")
    print("press ctrl c to exit")
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
