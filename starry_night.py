import board
import neopixel
import time
import random

BRIGHTNESS = .25
num_pixels = 30
np = neopixel.NeoPixel(board.A7, num_pixels, brightness=BRIGHTNESS, auto_write=False)

def starry_night(color1, color2, loop):
        np.fill(color1)
        np[int(num_pixels/2)] = color2
        np[int(num_pixels/2 + 1)] = color2
        np[int(num_pixels/2 - 1)] = color2
        np.show()
        for i in range(random.randint(0, int(num_pixels/6))):
            intensity = random.random() * 0.3 + 0.2
            foreground = [int(i * intensity) for i in color2]
            np[random.randint(0, num_pixels-1)] = foreground
        np.show()
        time.sleep(0.088)

while True:
    starry_night([2, 0, 13], [88, 88, 75], 10)
