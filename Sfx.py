from microbit import *
import radio
import random

def handle_radio_inputs():
    incoming = radio.receive()
    if incoming == 'init':
        display.show(':')
    if incoming == 'soon':
        display.show('s')
    if incoming == 'red':
        display.show('r')
    if incoming == 'amber':
        display.show('a')
    if incoming == 'green':
        display.show('g')
    if incoming == 'go':
        display.show('!')
    if incoming == 'p1pressed':
        display.show('<')
    if incoming == 'p2pressed':
        display.show('>')
    if incoming == 'p1won':
        display.show('1')
    if incoming == 'p2won':
        display.show('2')

radio.on()
radio.config(group=21)
display.scroll("sfx:21", 50)

while True:
    handle_radio_inputs()
    sleep(50)