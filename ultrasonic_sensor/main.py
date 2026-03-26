#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait



ev3 = EV3Brick()
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=.5, axle_track=104)



obstacle_sensor = UltrasonicSensor(Port.S4)
ev3.speaker.beep()
# Drive forward until something is closer than 300 mm (about 8 inches).

while True:
    distance = obstacle_sensor.distance()
    if distance < 300: #Getting too close
        ev3.speaker.beep(880, 200)
        robot.turn(520)
        robot.drive(360, 360)
    else:
        robot.drive(-150, 0)
    wait(10)