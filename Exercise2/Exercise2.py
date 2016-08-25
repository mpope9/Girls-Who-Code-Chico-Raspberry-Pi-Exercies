import RPIO

inputPin = 8
outputPin = 10

RPIO.setmode(RPIO.BOARD)

RPIO.setup(inputPin, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(outputPin, RPIO.OUT, initial=RPIO.LOW)

# Busy loop
while True:
    buttonPressed = RPIO.input(inputPin)
    # This means the button has been pressed
    if buttonPressed == False:
        # Reads the status of the output pin
        if RPIO.input(outputPin):
            RPIO.output(outputPin, RPIO.HIGH)
        else:
            RPIO.output(outputPin, RPIO.LOW)
