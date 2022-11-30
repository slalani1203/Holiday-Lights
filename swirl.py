import board
import neopixel
import time
import random

BRIGHTNESS = .25
num_pixels = 30
np = neopixel.NeoPixel(board.A7, num_pixels, brightness=BRIGHTNESS, auto_write=False)

colors = ([255,255,255], [255,255,255], [255,0,0], [255,0,0])

def swirl(color1, color2, loop, count, delay):
    result = 0
    for i in range(count * loop):
        intensity = random.random() * 0.3 + 0.5
        filling = [int(i * intensity) for i in color1]
        np.fill(filling)
        for k in range(num_pixels):
            if k % count == result:
                np[k] = color2
                np[k-1] = color2
        np.show()
        time.sleep(delay)
        result += 1
        result %= count

while True:
    swirl(colors[0], colors[2], 20, len(colors), 0.2)
