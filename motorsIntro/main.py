#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait

ev3 = EV3Brick()

motor = Motor(Port.B)
"""
#Run forward at 360 degrees per second for 2 seconds, then brake.
ev3.speaker.beep()
motor.run(360)
wait(2000)
motor.stop(Stop.BRAKE)
"""
"""
#Run forward at 360 degrees per second for 360 degrees, then reverse for 360 degrees, then forward 90 degrees.
motor.run_angle(360,360)
wait(500)
motor.run_angle(360, -360)
wait(500)
motor.run_angle(360, 90)
"""
"""
#Stop the motor with the brake.
motor.stop(Stop.BRAKE)
"""
"""
for i in range(8):
    ev3.speaker.beep()
    wait(100)
"""
"""
#Challenge 1
for i in range(3):
    motor.run_angle(360, 180)
    wait(500)
    motor.run_angle(360, -180)
    wait(500)

ev3.speaker.beep(880, 500)
for i in range(3):
    ev3.speaker.beep()
    wait(100)
ev3.speaker.beep(880, 500)
"""
#Challenge 2
ev3.screen.clear()
ev3.speaker.say("Clock Hand")
ev3.speaker.beep()

ev3.screen.print("12 oclock")
wait(1000)
ev3.screen.print("3 oclock")
motor.run_target(360, 90)
wait(1000)
ev3.screen.print("6 oclock")
motor.run_target(360, 180)
wait(1000)
ev3.screen.print("9 oclock")
motor.run_target(360, 270)
wait(1000)
ev3.screen.print("12 oclock")
motor.run_target(360, -270)
motor.hold()
ev3.screen.print("Done!")
wait(10000)

# Move to each position in order: 0, 90, 180, 270, back to 0
# At each position:
# - Print the position name (e.g., "12 oclock", "3 oclock", etc.)
# - Wait 1000 ms before moving to the next one
# Use run_target() for each move
# End with motor.hold()