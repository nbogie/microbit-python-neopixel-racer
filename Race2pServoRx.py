from microbit import *
import radio

# Don't ask it to go to 0 - may stop whole thing

def player1WinWiggle():
    wiggleBetween(15, 5, 4)

def player2WinWiggle():
    wiggleBetween(165, 175, 4)

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
        player1WinWiggle()
    elif (msg == "p2won"):
        player2WinWiggle()

def toggleMarkerPixel():
    pass

def preGameWiggle():
    pin1.write_analog(175)
    sleep(500)
    pin1.write_analog(5)
    sleep(500)
    pin1.write_analog(90)

def wiggleBetween(angle1, angle2, repetitions):
    for i in range(repetitions):
        pin1.write_analog(angle1)
        sleep(300)
        pin1.write_analog(angle2)
        sleep(300)


def demo():
    while True:
        pin1.write_analog(180)
        sleep(1000)
        pin1.write_analog(1)
        sleep(1000)    

radio.on()
radio.config(group=21)
display.show('s')
sleep(500)

pin1.set_analog_period(20)
# demo()
while True:
    incoming = radio.receive()
    if incoming is not None:
        processMsg(incoming)
        toggleMarkerPixel()
    sleep(50)  # conserve batt?