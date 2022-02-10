#!/usr/bin/env python3
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
    tank_drive = MoveSteering(OUTPUT_A, OUTPUT_D)
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Completing Maze...')

    # print something to the output panel in VS Code
    debug_print('Running')

    tank_drive.on(0, SpeedPercent(75))

    while not e_stop.value():
        distance = distance_sensor.value() / 10
        while distance <= 15:
            tank_drive.on_for_seconds(0, -75, 1)
            tank_drive.on_for_seconds(100-200*random.randint(0, 1), 75, 0.7)


if __name__ == '__main__':
    main()
