import RPIO

inputPin = 8
outputPin1 = 10
outputPin2 = 12

RPIO.setmode(RPIO.BOARD)

# Out1 is off, Out2 is on.
RPIO.setup(inputPin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(outputPin1, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(outputPin2, RPIO.OUT, initial=RPIO.HIGH)

# Busy loop
while True:
    buttonPressed = RPIO.input(inputPin)
    if buttonPressed:
        if RPIO.input(outputPin1):
            RPIO.output(outputPin1, RPIO.HIGH)
            RPIO.output(outputPin2, RPIO.LOW)
        else:
            RPIO.output(outputPin1, RPIO.LOW)
            RPIO.output(outputPin2, RPIO.HIGH)
