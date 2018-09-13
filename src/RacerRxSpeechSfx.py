from microbit import *
import radio
import random
import music
import speech


def handle_radio_inputs():
    incoming = radio.receive()
    if incoming == 'init':
        display.show(':')
        music.play(music.JUMP_UP)
        speech.say("System Initialising")
    if incoming == 'soon':
        display.show('s')
    if incoming == 'red':
        speech.say("Ready")
        #music.pitch(880, 30)
        display.show('r')
    if incoming == 'amber':
        speech.say("Steady")        
        #music.pitch(880, 30)
        display.show('a')
    if incoming == 'green':
        speech.say("Green, green, green!")
        music.pitch(1760, 120)
        display.show('g')
    if incoming == 'go':
        display.show('!')
        #speech.say("Go")
        music.play(music.BA_DING)        
    if incoming == 'p1moved':
        display.show('<')
        music.pitch(660, 30)        
    if incoming == 'p2moved':
        display.show('>')
        music.pitch(440, 30)
    if incoming == 'p1won':
        display.show('1')
        speech.say("Congratulations Player One!")
        music.play(music.POWER_UP)
    if incoming == 'p2won':
        display.show('2')
        speech.say("Congratulations Player Two!")
        music.play(music.JUMP_DOWN)

radio.on()
radio.config(group=21)
display.scroll("sfx:21", 50)
music.set_tempo(ticks=4, bpm=240)

while True:
    handle_radio_inputs()
    sleep(10)