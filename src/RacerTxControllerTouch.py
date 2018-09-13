from microbit import *
import radio

# Don't change this, you will need it
already = [False, False, False]
def was_touched(pinNum):
    global already
    pin = [pin0, pin1, pin2][pinNum]
    t = pin.is_touched()
    result = t and not already[pinNum]
    already[pinNum] = t
    return result


#Your code goes here
radio.config(group=21)
radio.on()
display.scroll('Ctrl. Ch 21', 50)

while True:
    if (was_touched(0)):
        radio.send("start")
        display.show('0')
    if (was_touched(1)):
        radio.send("a")
        display.show('1')
    if (was_touched(2)):
        radio.send("b")
        display.show('2')
    if button_a.was_pressed():
        radio.send("a")
        display.show("a")
    if button_b.was_pressed():
        radio.send("b")
        display.show("b")
    if accelerometer.was_gesture("shake"):
        radio.send("start")
        display.show("!")
    sleep(20)