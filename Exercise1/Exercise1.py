import RPIO
import time

pin = 8

RPIO.setmode(RPIO.BOARD)

RPIO.setup(pin, RPIO.OUT)

# Busy loop that uses 2 seconds per iteration
while True:
    RPIO.output(pin, RPIO.HIGH)
    time.sleep(1)
    RPIO.output(pin, RPIO.LOW)
    time.sleep(1)

RPIO.cleanup()
