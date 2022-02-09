#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TougtchSensor, UltrasonicSensor

import os
import sys
import time

# state constants
ON = True
OFF = False


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
    # set the console just how we want it
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-Terminus24x12')

    # print something to the screen of the device
    print('Completing Maze...')

    # print something to the output panel in VS Code
    debug_print('Running')

    # wait a bit, so you have time to look at the display before the program
    # exits
    time.sleep(5)


if __name__ == '__main__':
    main()
