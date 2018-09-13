from microbit import *
import radio
import music

WIN_SONG_2 = ['E5:2', 'R:4', 'G:2', 'R:4', 'E:2', 'R:2', 
              'E:2',  'R:4', 'G:2', 'R:4', 'E:2', 'R:2', 
              'E:2',  'R:4', 'G:2', 'R:4', 'E:2', 'R:2',                 
              'F#:2', 'R:4', 'E:2', 'R:4', 'D:2', 'R:2']
            

def handle_radio_inputs():
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


radio.on()
radio.config(group=21)
display.scroll("sfx:21", 50)
music.set_tempo(ticks=4, bpm=240)

while True:
    handle_radio_inputs()
    sleep(10)