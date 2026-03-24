#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor = Motor(Port.A)
button1 = TouchSensor(Port.S4)
color_sensor = ColorSensor(Port.S3)

#Variables
i = 0

while True:
    if button1.pressed():
        ev3.speaker.beep()
        i += 1
        ev3.screen.print(i)
        wait(500)
        if(i == 5):
            ev3.screen.print("You win!")
            motor.run_time(360, 2000)
            break
    if color_sensor.color() != None:
        ev3.screen.print(str(color_sensor.color()) + " Detected!")
        for i in range(3):
            ev3.speaker.beep()
            wait(500)

ev3.screen.print("Program Exited!")
    
