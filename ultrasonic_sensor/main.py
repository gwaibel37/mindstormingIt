#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)
obstacle_sensor = UltrasonicSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=104)
robot.settings(800, 1000, 400, 800)

# --- Ramming Mode --- #
def ramming_mode():
    ev3.speaker.beep(880, 200)
    ev3.light.on(Color.RED)
    robot.drive(-800, 0)
    wait(2000)          # Ram for 2 seconds
    robot.stop()
    ev3.light.off()

# --- Obstacle Handling --- #
def obstacle_detect(distance):
    if distance < 350:
        ramming_mode()
        wait(300)
        ev3.speaker.beep(880, 100)
        # Controlled backup AFTER ramming
        robot.straight(500)   # Back up 500 mm
        # Turn around
        robot.turn(520)
    else:
        robot.drive(-200, 0)

def flash():
    ev3.light.on(Color.BLUE)
    wait(100)
    ev3.light.off()

while True:
    distance = obstacle_sensor.distance()
    obstacle_detect(distance)
    flash()
    wait(50)
