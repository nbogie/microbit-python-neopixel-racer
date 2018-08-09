# colour-match space invaders
from microbit import *
import neopixel
import speech

RED = (64, 0, 0)
GREEN = (0, 64, 0)
BLUE = (0, 0, 64)
yellow = (64, 24, 0)
off = (0, 0, 0)


class Player:

    def __init__(self, colour, max_pos):
        self.pos = 0
        self.colour = colour
        self.max_pos = max_pos

    def update(self):
        print("updating")

    def draw(self, neopixels):
        neopixels[self.pos] = self.colour

    def move_forward(self):
        self.pos = self.pos + 1
        if (self.pos > self.max_pos):
            self.pos = self.max_pos


class Game:
    def __init__(self):
        self.button_pins = [pin12, pin15, pin14, pin16]
        self.ledcols = [RED, BLUE, GREEN, yellow]
        self.num_pixels = 6
        self.npix = neopixel.NeoPixel(pin13, self.num_pixels)
        self.players = [Player(RED, self.num_pixels - 1),
                        Player(BLUE, self.num_pixels - 1)]
        self.game_over = False

    def check_for_win(self):
        return False

    def move_players(self):
        if (pin16.read_digital()):
            self.players[0].move_forward()
        if (pin15.read_digital()):
            self.players[1].move_forward()

        for p in self.players:
            p.update()

    def update(self):
        self.frame_delay = (int)(500 * (pin0.read_analog() / 200))
        self.move_players()
        self.check_for_win()

    def draw_game_over():
        self.npix[0] = (100,100,100)
        speech.say("game over")

    def draw(self):
        if(self.game_over):
            draw_game_over()
        else:
            for p in self.players:
                p.draw(self.npix)
        self.npix.show()

    def game_loop(self):
        speech.say("starting!")
        while True:
            self.update()
            self.draw()
            sleep(self.frame_delay)


game = Game()
game.game_loop()
