from microbit import *
import radio
import music
import speech


def handle_radio_inputs():
    incoming = radio.receive()
    if incoming == 'init':
        display.show('!')
        music.play(music.JUMP_UP)
        speech.say("System Initialising")
    if incoming == 'red':
        speech.say("Ready")
        display.show('r')
    if incoming == 'amber':
        speech.say("Steady")        
        display.show('a')
    if incoming == 'green':
        speech.say("Go, go, Go!")
        display.show('g')
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
        music.play(music.POWER_UP)

radio.on()
radio.config(group=21)
display.scroll("speech:21", 50)

while True:
    handle_radio_inputs()
    sleep(10)