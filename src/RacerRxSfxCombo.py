from microbit import *
import radio
import music
import speech

# This is not the best example to learn from, 
# because it combines two demonstration modes.
# Instead, look at RacerRxSfx.py and RacerRxSpeechSfx.py

# Here's the data for a custom song we'll play when p2 wins

WIN_SONG_2 = ['E5:2', 'R:4', 'G:2', 'R:4', 'E:2', 'R:2', 
              'E:2',  'R:4', 'G:2', 'R:4', 'E:2', 'R:2', 
              'E:2',  'R:4', 'G:2', 'R:4', 'E:2', 'R:2',                 
              'F#:2', 'R:4', 'E:2', 'R:4', 'D:2', 'R:2']

def handle_radio_inputs_no_speech():
    incoming = radio.receive()
    if incoming == 'init':
        display.show(':')
        music.play(music.JUMP_UP)
    if incoming == 'red':
        music.pitch(880, 30)
        display.show('r')
    if incoming == 'amber':
        music.pitch(880, 30)
        display.show('a')
    if incoming == 'green':
        music.pitch(1760, 120)
        display.show('g')
    if incoming == 'go':
        display.show('!')
        music.play(music.BA_DING)        
    if incoming == 'p1moved':
        display.show('<')
        music.pitch(660, 30)        
    if incoming == 'p2moved':
        display.show('>')
        music.pitch(440, 30)
    if incoming == 'p1won':
        display.show('1')
        music.play(music.POWER_UP)
    if incoming == 'p2won':
        display.show('2')
        music.play(WIN_SONG_2)        


def handle_radio_inputs_with_speech():
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

speech_on = button_b.is_pressed()

if speech_on:
    display.scroll("Speech ON", 50)
else:
    display.scroll("Speech OFF", 50)

display.scroll("SFX Combo:21", 50)
music.set_tempo(ticks=4, bpm=240)
    
while True:
    if (speech_on):
        handle_radio_inputs_with_speech()
    else:
        handle_radio_inputs_no_speech()            
    sleep(10)