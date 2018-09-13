from microbit import *

# Don't change this, you will need it
already = [False, False, False]
def was_touched(pinNum):
    global already
    pin = [pin0, pin1, pin2][pinNum]
    t = pin.is_touched()
    result = t and not already[pinNum]
    already[pinNum] = t
    return result


# Your code goes here...

while True:
    if was_touched(0):
        display.show('0')
