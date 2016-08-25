import RPIO

# Unsure if all of these pins are GPIO...
inputPin = 8
outputPin1 = 10
outputPin2 = 12
outputPin3 = 14
outputPin4 = 16

RPIO.setmode(RPIO.BOARD)

RPIO.setup(inputPin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(outputPin1, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(outputPin2, RPIO.OUT, initial=RPIO.HIGH)
RPIO.setup(outputPin3, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(outputPin4, RPIO.OUT, initial=RPIO.HIGH)

# Busy loop
while True:
    buttonPressed = RPIO.input(inputPin)
    if buttonPressed:
        if RPIO.input(outputPin1):
            RPIO.output(outputPin1, RPIO.HIGH)
            RPIO.output(outputPin3, RPIO.HIGH)
            RPIO.output(outputPin2, RPIO.LOW)
            RPIO.output(outputPin4, PRIO.LOW)
        else:
            RPIO.output(outputPin2, RPIO.HIGH)
            RPIO.output(outputPin4, RPIO.HIGH)
            RPIO.output(outputPin1, RPIO.LOW)
            RPIO.output(outputPIn3, RPIO.LOW)
