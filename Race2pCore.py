from microbit import *
import neopixel
import radio
import random

RED = (64, 0, 0)
GREEN = (0, 64, 0)
BLUE = (0, 0, 64)
YELLOW = (64, 24, 0)
ORANGE = (64, 64, 0)
off = (0, 0, 0)
colours = [RED, ORANGE, GREEN, BLUE, YELLOW]


class Player:

    def __init__(self, colour, max_pos):
        self.pos = 0
        self.colour = colour
        self.max_pos = max_pos
        self.finished = False

    def draw(self, pixels):
        pixels[self.pos] = self.colour

    def cycle_colour(self):
        self.colour = random.choice(colours)

    def move_forward(self):
        if not self.finished:
            self.pos = self.pos + 1
            if self.pos > self.max_pos:
                self.pos = self.max_pos
                self.finished = True

    def is_finished(self):
        return self.finished


class Game:
    STATE_FINISHED = 'finished'
    STATE_STARTING = 'starting'
    STATE_LIGHTS = 'lights'
    STATE_RACING = 'racing'

    def __init__(self):
        self.num_pixels = 59
        self.strips = self.create_pixel_strips(self.num_pixels)
        self.players = [Player(RED, self.num_pixels - 1), Player(BLUE, self.num_pixels - 1)]
        self.game_over = False
        self.dirty = [False, False]
        self.state = Game.STATE_STARTING
        self.winner_ix = 10
        self.clear_strips()

    def create_pixel_strips(self, num):
        #pin 13 for bit commander
        return [neopixel.NeoPixel(pin0, num), neopixel.NeoPixel(pin1, num)]

    def strip_show_colour(self, strip, colour):
        for i in range(self.num_pixels):
            strip[i] = colour
        strip.show()

    def clear_strips(self):
        for s in self.strips:
            s.clear()
            s.show()

    def start_race(self):
        self.state = Game.STATE_LIGHTS
        for (c, msg) in [(RED, 'red'), (ORANGE, 'amber'), (GREEN, 'green')]:
            radio.send(msg)
            for s in self.strips:
                self.strip_show_colour(s, c)
            sleep(500)
        self.clear_strips()

        self.state = Game.STATE_RACING
        radio.send('go')

    def handle_radio_inputs(self):
        incoming = radio.receive()
        if incoming == 'start':
            if self.state == Game.STATE_STARTING:
                self.start_race()

        if incoming == 'a':
            self.advance_player(0)

        if incoming == 'b':
            self.advance_player(1)

    def win_race(self, ix):
        self.winner_ix = ix
        radio.send("p1won" if ix == 0 else "p2won")
        # TODO: animate win by player colour
        self.state = Game.STATE_FINISHED

    def advance_player(self, ix):
        if self.state == Game.STATE_RACING:
            self.players[ix].move_forward()
            radio.send('p1moved' if ix == 0 else 'p2moved')

            if self.players[ix].is_finished():
                self.win_race(ix)
            self.dirty[ix] = True

    def spin_player_colour(self, ix):
        self.players[ix].cycle_colour()
        self.dirty[ix] = True

    def handle_inputs(self):
        self.handle_radio_inputs()

        if self.state == Game.STATE_STARTING:
            if button_a.is_pressed():
                # self.spin_player_colour(0)
                self.start_race()

            if button_b.is_pressed():
                self.spin_player_colour(1)
        else:
            if button_a.was_pressed():
                self.advance_player(0)
            if button_b.was_pressed():
                self.advance_player(1)

    def update(self):
        self.handle_inputs()

    def draw_game_over(self):
        for s in self.strips:
            s[1] = RED
            s[2] = GREEN
            s[3] = BLUE
            s.show()

    def redraw_dirty(self):
        if self.state == Game.STATE_FINISHED:
            self.draw_game_over()
        else:
            for i in range(2):
                if self.dirty[i]:
                    self.strips[i].clear()
                    # TODO: check strip is passed by reference
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
display.scroll("pyrace ch21", 50)
game.game_loop()