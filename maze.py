#!/usr/bin/env python3
from dis import dis
import random

from ev3dev2.motor import OUTPUT_A, OUTPUT_D, SpeedPercent, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor

import os
import sys

# state constants
ON = True
OFF = False

distance_sensor = UltrasonicSensor(INPUT_1)
e_stop = TouchSensor(INPUT_4)

distance_sensor.mode = 'US-DIST-CM'


def debug_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    print('\x1Bc', end='')


def set_cursor(state):
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    os.system('setfont ' + name)


def main():
    tank_drive = MoveSteering(OUTPUT_D, OUTPUT_A)
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus22x11')

    # print something to the screen of the device
    print('Completing Maze...')

    # print something to the output panel in VS Code
    debug_print('Running')

    tank_drive.on(0, SpeedPercent(100))
    last3_numbers = [100, 100, 100]
    multiply = 1
    direction = -100
    while not e_stop.value():
        distance = round(distance_sensor.value())
        distance_average = round(sum(last3_numbers, distance)/4)
        if distance_average <= 15 and distance != 0 and distance_average != 0:
            tank_drive.off()
            debug_print(multiply)
            if multiply == 2:
                direction = direction * -1
            tank_drive.on_for_seconds(0, SpeedPercent(-75), 0.1)
            tank_drive.on_for_seconds(direction, SpeedPercent(75), 0.86 * multiply)
            multiply = 2
            tank_drive.off()
        else:
            tank_drive.on(0, SpeedPercent(100))
            multiply = 1
            direction = -100
        if distance == 0:
            return
        last3_numbers[0] = last3_numbers[1]
        last3_numbers[1] = last3_numbers[2]
        last3_numbers[2] = distance

if __name__ == '__main__':
    main()
