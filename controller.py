from microbit import *
import radio

radio.config(group=22)
radio.on()

count = 0
while True:
    if accelerometer.was_gesture("shake"):
        radio.send("start")
        display.show("s")
        count += 1
    if button_a.was_pressed():
        radio.send("a")
        display.show("a")
        count += 1
    if button_b.was_pressed():
        radio.send("b")
        display.show("b")
        count += 1