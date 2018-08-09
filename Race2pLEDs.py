from microbit import *
import neopixel
import radio
from random import random

RED = (64, 0, 0)
GREEN = (0, 64, 0)
BLUE = (0, 0, 64)
yellow = (64, 24, 0)
off = (0, 0, 0)


class ColorUtils:
    @staticmethod
    def random_colour():
        rgb = ColorUtils.hsv_to_rgb_256(random(), 1, 1)
        return rgb[0], rgb[1], rgb[2], 255

    @staticmethod
    def hsv_to_rgb_256(h, s, v):
        tmp = ColorUtils.hsv_to_rgb(h, s, v)
        return int(tmp[0] * 255), int(tmp[1] * 255), int(tmp[2] * 255)

    @staticmethod
    def hsv_to_rgb(h, s, v):
        if s == 0.0:
            return v, v, v
        i = int(h * 6.0)  # XXX assume int() truncates!
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0:
            return v, t, p
        if i == 1:
            return q, v, p
        if i == 2:
            return p, v, t
        if i == 3:
            return p, q, v
        if i == 4:
            return t, p, v
        if i == 5:
            return v, p, q


class Player:

    def __init__(self, hue360, max_pos):
        self.pos = 0
        self.hue360 = hue360
        self.colour = ColorUtils.hsv_to_rgb_256(self.hue360 / 360.0, 100, 100)
        self.max_pos = max_pos
        self.finished = False

    def draw(self, pixels):
        pixels[self.pos] = self.colour

    def inc_colour(self, inc):
        self.hue360 = (self.hue360 + inc) % 360
        self.colour = ColorUtils.hsv_to_rgb_256(self.hue360 / 360.0, 100, 100)

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
    STATE_RACING = 'racing'

    def __init__(self):
        self.button_pins = [pin12, pin15, pin14, pin16]
        self.led_colours = [RED, BLUE, GREEN, yellow]
        self.num_pixels = 6
        self.strips = self.create_pixel_strips(self.num_pixels)
        self.players = [Player(RED, self.num_pixels - 1), Player(BLUE, self.num_pixels - 1)]
        self.game_over = False
        self.dirty = [False, False]
        self.state = Game.STATE_STARTING

    def create_pixel_strips(self, num):
        return [neopixel.NeoPixel(pin13, num), neopixel.NeoPixel(pin11, num)]

    def check_for_win(self):
        return False

    def start_race(self):
        self.state = Game.STATE_RACING

    def handle_radio_inputs(self):
        incoming = radio.receive()
        if incoming == 'start':
            print("radio says start")
            if self.state == Game.STATE_STARTING:
                self.start_race()

        if incoming == 'a':
            print("radio says move a")
            self.advance_player(0)

        if incoming == 'b':
            print("radio says move b")
            self.advance_player(1)

    def advance_player(self, ix):
        if self.state == Game.STATE_RACING:
            self.players[ix].move_forward()
            if self.players[ix].is_finished():
                self.state = Game.STATE_FINISHED
            self.dirty[ix] = True

    def spin_player_colour(self, ix):
        self.players[ix].inc_colour(5)
        self.dirty[ix] = True

    def handle_inputs(self):
        self.handle_radio_inputs()

        if self.state == Game.STATE_STARTING:
            if button_a.is_pressed():
                self.spin_player_colour(0)
            if button_b.is_pressed():
                self.spin_player_colour(1)
        else:
            if pin16.read_digital():
                self.advance_player(0)
            if pin15.read_digital():
                self.advance_player(1)

    def update(self):
        self.handle_inputs()
        self.check_for_win()

    def draw_game_over(self):
        for s in self.strips:
            s[1] = (200, 0, 200)
            s[2] = (0, 200, 200)
            s[3] = (0, 0, 200)
            s.show()

    def redraw_dirty(self):
        if self.state == Game.STATE_FINISHED:
            self.draw_game_over()
        else:
            for i in range(2):
                if self.dirty[i]:
                    # TODO: check strip is passed by reference
                    self.players[i].draw(self.strips[i])
                    self.dirty[i] = False

        for s in self.strips:
            s.show()

    def game_loop(self):
        while True:
            
            self.update()
            self.redraw_dirty()


radio.on()
radio.config(group=22)
radio.send('i_am_awake')
game = Game()
game.game_loop()