import RPIO

inputPin1 = 8
inputPin2 = 10
outputPin = 12

# Sequence that should be matched
solution = array(1, 2, 1, 2, 1, 1, 2, 2)

# The user's guess
attempt = array()

RPIO.setup(inputPin1, RPIO.IN, pull_up_down=RPIO.PUD_UP)
RPIO.setup(inputPin2, RPIO.IN, pull_up_down=RPIO.PUD_UP)
PRIO.setup(outputPin, RPIO.OUT, initial=RPIO.LOW)

# Busy loop
while True:
    # Bonus restart
