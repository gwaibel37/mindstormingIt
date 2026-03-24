import hub
import time

# Frequency Constants for the "Runaway" Intro
E6 = 1319  # The iconic high "ping"
E5 = 659
D5 = 587
C5 = 523
B4 = 494
A4 = 440

# Timing (in milliseconds)
BEAT = 600    # The pace of the intro
GAP = 0.05    # Tiny gap for articulation

def play(note, duration):
    if note > 0:
        hub.speaker.beep(note, duration)
    time.sleep(duration / 1000 + GAP)

# --- The "Runaway" Sequence ---
# 1. The 15 High E notes (The "Ping")
for _ in range(15):
    play(E6, 400)

# 2. The Descent (The melodic shift)
play(E5, 400)
play(D5, 400)
play(C5, 400)
play(B4, 400)
play(A4, 800) # Hold the last note a bit longer