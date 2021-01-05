from adafruit_circuitplayground import cp
import time

OFF = (0, 0, 0)
RED = (30, 0, 0)
BLUE = (0, 0, 30)

def snake(start_pos, length, R = 30, G = 0, B = 0):
    color = (R, G, B)
    while True:
        for i in range(length):
            cp.pixels[(start_pos+i)%10] = color
        time.sleep(.1)
        cp.pixels.fill(OFF)
        start_pos = start_pos + 1
        if cp.button_a == True:
            while cp.button_a == True:
                print('Unpush the button')
                time.sleep(.2)
            length = length - 1

snake(0, 4)

def snake_game(start_pos, length, R = 30, G = 0, B = 0):
    color = (R, G, B)
    while True:
        for i in range(length):
            cp.pixels[(start_pos+i)%10] = color
        time.sleep(.05)
        while cp.button_a == True:
            if cp.pixels[2] == color:
                cp.pixels.fill(BLUE)
                time.sleep(.1)
            else:
                cp.pixels.fill(RED)
                time.sleep(.1)
        cp.pixels.fill(OFF)
        start_pos = start_pos + 1

#snake_game(0, 4)
