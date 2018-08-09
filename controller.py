from microbit import *
import radio

radio.config(group=22)
radio.on()

count = 0
while True:
    if button_a.was_pressed():
        radio.send("a")
        display.show("a")
        count += 1
    if button_b.was_pressed():
        radio.send("b")
        display.show("b")
        count += 1