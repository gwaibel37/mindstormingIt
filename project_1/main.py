#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait
# Create the EV3Brick object. We need this in every program.
ev3 = EV3Brick()
# -------------------------------------------------------
# SCREEN
# -------------------------------------------------------
# Clear the screen so it's blank before we write anything.
ev3.screen.clear()
# Print lines of text on the EV3 display.
# Each call to print() adds a new line, just like Python's built-in print().
ev3.screen.print("Hello, World!")
ev3.screen.print("EV3 is ready.")
# -------------------------------------------------------
# STATUS LIGHT
# -------------------------------------------------------
# Change the status light color.
# Options: Color.GREEN, Color.RED, Color.ORANGE                                                               
ev3.light.on(Color.ORANGE)
# -------------------------------------------------------
# SPEAKER
# -------------------------------------------------------
# beep(frequency, duration)
# frequency → pitch in Hz. Higher number = higher pitch.
# 440 Hz is the musical note A4 (standard tuning pitch).
# duration → how long the beep lasts, in milliseconds.
# 500 ms = half a second.
ev3.speaker.beep(440, 500)
# wait() pauses the program for a set number of milliseconds.
# 1000 ms = 1 second.
wait(1000)
# Play a second beep at a higher pitch.
ev3.speaker.beep(880, 500) # 880 Hz is exactly one octave above 440 Hz
wait(1000)
# -------------------------------------------------------
# WRAP UP
# -------------------------------------------------------
# Turn the light green to signal the program finished successfully.
ev3.light.on(Color.GREEN)
ev3.screen.print("Done!")
# Wait 2 seconds so we can read the screen before the program exits.
wait(2000)