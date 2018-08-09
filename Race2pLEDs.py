from microbit import *
import neopixel
import radio


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

    def draw(self, pixels):
        pixels[self.pos] = self.colour
        #pixels[self.pos - 1] = self.colour

    def move_forward(self):
        self.pos = self.pos + 1
        if self.pos > self.max_pos:
            self.pos = self.max_pos


class Game:
    def __init__(self):
        self.button_pins = [pin12, pin15, pin14, pin16]
        self.led_colours = [RED, BLUE, GREEN, yellow]
        self.num_pixels = 6
        self.strips = self.create_pixel_strips(self.num_pixels)
        self.players = [Player(RED, self.num_pixels - 1), Player(BLUE, self.num_pixels - 1)]
        self.game_over = False
        self.dirty = [2]

    def create_pixel_strips(self, num):
        return [neopixel.NeoPixel(pin13, num)]

    def check_for_win(self):
        return False

    def handle_radio_inputs(self):
        print("handling radio inputs")
        incoming = radio.receive()
        if incoming == 'start':
            print("radio says start")
        if incoming == 'a':
            print("radio says move a")
        if incoming == 'b':
            print("radio says move b")

    def handle_inputs(self):
        self.handle_radio_inputs()
        if button_a.was_pressed():
            print("button a pressed")

        if pin16.read_digital():
            self.players[0].move_forward()
            self.dirty[0] = True
        if pin15.read_digital():
            self.players[1].move_forward()
            self.dirty[1] = True

    def update(self):
        self.handle_inputs()
        self.check_for_win()

    def draw_game_over(self):
        self.strips[0][3] = (200, 0, 200)

    def redraw_dirty(self):
        if self.game_over:
            self.draw_game_over()
        else:
            for i in range(2):
                if self.dirty[i]:
                    self.players[i].draw(self.num_pixels)
                    self.dirty[i] = False

        for s in self.strips:
            s.show()

    def game_loop(self):
        while True:
            
            self.update()
            self.redraw_dirty()


radio.on()
radio.send('i_am_awake')
game = Game()
game.game_loop()
