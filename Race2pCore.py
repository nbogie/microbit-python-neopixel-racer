from microbit import *
import neopixel
import radio

L=150
RED = (L, 0, 0)
GREEN = (0, L, 0)
BLUE = (0, 0, L)
AMBER = (L, L, 0)

def less(v):
    return max(0, v-29)


def softer(c):
    return tuple(map(less, c))


class Player:

    def __init__(self, colour, max_pos):
        self.pos = 0
        self.colour = colour
        self.max_pos = max_pos
        self.finished = False

    def reset(self):
        self.pos = 0
        self.finished = False

    def draw(self, pixels):
        pixels[self.pos] = self.colour
        if self.pos > 1:
            pixels[self.pos - 1] = softer(self.colour)
        if self.pos > 2:
            pixels[self.pos - 2] = softer(softer(self.colour))

    def move_forward(self):
        if not self.finished:
            self.pos = self.pos + 1
            if self.pos > self.max_pos:
                self.pos = self.max_pos
                self.finished = True

    def is_finished(self):
        return self.finished


class Game:
    STATE_FINISHED = 'f'
    STATE_STARTING = 's'
    STATE_LIGHTS = 'l'
    STATE_RACING = 'r'

    def __init__(self):
        self.num_pixels = 59
        self.strips = self.create_pixel_strips(self.num_pixels)
        self.players = [Player(RED, self.num_pixels - 1), Player(BLUE, self.num_pixels - 1)]
        self.dirty = [False, False]
        self.state = Game.STATE_STARTING
        self.clear_strips()

    def create_pixel_strips(self, num):
        return [neopixel.NeoPixel(pin0, num), neopixel.NeoPixel(pin1, num)]

    def strip_show_colour(self, strip, colour, maxPxl=59):
        for i in range(min(self.num_pixels, maxPxl)):
            strip[i] = colour
        strip.show()

    def clear_strips(self):
        for s in self.strips:
            s.clear()
            s.show()

    def start_race(self):
        self.state = Game.STATE_LIGHTS
        for (c, msg) in [(RED, 'red'), (AMBER, 'amber'), (GREEN, 'green')]:
            radio.send(msg)
            for s in self.strips:
                self.strip_show_colour(s, c, 20)
            sleep(1000)
        self.clear_strips()
        self.state = Game.STATE_RACING
        radio.send('go')
        self.dirty = [True, True]

    def handle_radio_inputs(self):
        incoming = radio.receive()
        if incoming == 'start':
            if self.state == Game.STATE_STARTING:
                self.start_race()

        if incoming == 'a':
            self.advance_player(0)

        if incoming == 'b':
            self.advance_player(1)

    def advance_player(self, ix):
        if self.state == Game.STATE_RACING:
            self.players[ix].move_forward()
            radio.send('p1moved' if ix == 0 else 'p2moved')
            if self.players[ix].is_finished():
                self.state = Game.STATE_FINISHED
                radio.send("p1won" if ix == 0 else "p2won")
                for i in range(4):
                    for s in self.strips:
                        self.strip_show_colour(s, self.players[ix].colour)
                    sleep(200)
                    self.clear_strips()
                    sleep(200)
                sleep(3000)
                self.state = Game.STATE_STARTING
                for p in self.players:
                    p.reset()
            else:
                if self.players[0].pos > self.players[1].pos:
                    radio.send("p1lead")
                elif self.players[0].pos < self.players[1].pos:
                    radio.send("p2lead")
                else:
                    radio.send("tied")
                    
                
            self.dirty[ix] = True

    def handle_inputs(self):
        self.handle_radio_inputs()

        if self.state == Game.STATE_STARTING:
            if button_a.is_pressed():
                self.start_race()
        else:
            if button_a.was_pressed():
                self.advance_player(0)
            if button_b.was_pressed():
                self.advance_player(1)

    def update(self):
        self.handle_inputs()

    def redraw_dirty(self):
        if self.state == Game.STATE_FINISHED:
            pass
        else:
            for i in range(2):
                if self.dirty[i]:
                    self.strips[i].clear()
                    self.players[i].draw(self.strips[i])
                    self.dirty[i] = False

                    self.strips[i].show()

    def game_loop(self):
        while True:
            self.update()
            self.redraw_dirty()

radio.on()
radio.config(group=21)
radio.send('init')
game = Game()
display.scroll("core:21  ", 50)
display.scroll(L, 50)
game.game_loop()