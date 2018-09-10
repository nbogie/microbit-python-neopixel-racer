from microbit import *
import radio

# Note: Don't ask servo to go to 0 or 180.

def processMsg(msg):
    if (msg == "init"):
        preGameWiggle()
    elif (msg == "red"):
        pin1.write_analog(90)
    elif (msg == "p1lead"):
        pin1.write_analog(135)
    elif (msg == "p2lead"):
        pin1.write_analog(45)
    elif (msg == "tied"):
        pin1.write_analog(90)
    elif (msg == "p1won"):
        # pin1.write_analog(170)
        player1WinWiggle()
    elif (msg == "p2won"):
        # pin1.write_analog(10)
        player2WinWiggle()

def toggleMarkerPixel():
    display.set_pixel(0, 0, not display.get_pixel(0, 0))

def player1WinWiggle():
    wiggleBetween(175, 115, 4)

def player2WinWiggle():
    wiggleBetween(45, 5, 4)


def preGameWiggle():
    pin1.write_analog(175)
    sleep(500)
    pin1.write_analog(5)
    sleep(500)
    pin1.write_analog(90)

def wiggleBetween(angle1, angle2, repetitions):
    for i in range(repetitions):
        pin1.write_analog(angle1)
        sleep(500)
        pin1.write_analog(angle2)
        sleep(500)

radio.on()
radio.config(group=21)
display.scroll('servo 21', 50)
sleep(500)

pin1.set_analog_period(20)

while True:
    incoming = radio.receive()
    if incoming is not None:
        processMsg(incoming)
        toggleMarkerPixel()
    sleep(50)  # conserve batt?