# This is how to import modules in python. There are other modules, like 
# 'time' and 'os'.  There are documentation available to use for those too!
import RPIO as rpio

# Changes the numbering system for the GPIO ports.  There is another 
# numbering method, but you cannot mix them.  Unexpected behavior would
# happen.
rpio.setmode(rpio.BOARD)

# This is how to set up set up pin #8 as an output channel.
# This is also how you can use a method from a module, using the '.'
rpio.setup(8, rpio.OUT)

# Set the pin to "high"
rpio.output(8, True)

# CODE HERE

# Here is a cleanup method, many modules include one of these
# and they are suggested to be used.
rpio.cleanup()
