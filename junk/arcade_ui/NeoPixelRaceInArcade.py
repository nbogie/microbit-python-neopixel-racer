import arcade
from random import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400


class RaceState:
    def __init__(self, num_pixels):
        self._num_pixels = num_pixels
        self._player1_pos = 0
        self._player2_pos = 0
        self._is_started = False

    def num_pixels(self):
        return self._num_pixels

    def start(self):
        self._is_started = True

    def is_started(self):
        return self._is_started

    def reset(self):
        self._player1_pos = 0
        self._player2_pos = 0

    def advance_a(self):
        if self.is_started():
            self._player1_pos += 1

    def advance_b(self):
        if self.is_started():
            self._player2_pos += 1

    def player1_pos(self):
        return self._player1_pos

    def player2_pos(self):
        return self._player2_pos

    def player_positions(self):
        return self.player1_pos(), self.player2_pos()


class NeoPixelsSimulated:

    def __init__(self, num_pixels):
        self._num_pixels = num_pixels
        self._pixels = [(0, 0, 0, 0)] * num_pixels

    def num_pixels(self):
        return self._num_pixels

    def pixel_at(self, ix):
        return self._pixels[ix]

    def set_pixel_at(self, ix, color):
        if ix < self._num_pixels:
            self._pixels[ix] = color

    def set_all(self, color):
        for i in range(self._num_pixels):
            self._pixels[i] = color

    def clear(self):
        self.set_all((0, 0, 0, 0))


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


class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        num_pixels = 30
        self.sim1 = NeoPixelsSimulated(num_pixels)
        self.sim2 = NeoPixelsSimulated(num_pixels)

        self.raceState = RaceState(num_pixels)
        self.p1Color = ColorUtils.random_colour()
        self.p2Color = ColorUtils.random_colour()

        arcade.set_background_color(arcade.color.WHEAT)
        self.set_update_rate(1 / 50)
        self.test_colour = arcade.color.BABY_BLUE
        self.hue = 0.0


    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def draw_pixels(self, pixels, y):
        num_pixels = pixels.num_pixels()
        x_step = 800 / num_pixels

        arcade.draw_circle_filled(20, 20, 100, self.test_colour)

        x = x_step / 2
        for i in range(num_pixels):
            color = pixels.pixel_at(i)
            arcade.draw_circle_filled(x, y, x_step / 2, color)
            arcade.draw_circle_outline(x, y, x_step / 2 - 2, arcade.color.WHEAT, 2)

            x = x + x_step

    def on_draw(self):

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        arcade.start_render()
        self.draw_pixels(self.sim1, 250)
        self.draw_pixels(self.sim2, 200)


    # Call draw() on all your sprite lists below

    def update(self, delta_time):
        p1pos, p2pos = self.raceState.player_positions()
        self.sim1.clear()
        self.sim2.clear()

        self.sim1.set_pixel_at(p1pos, self.p1Color)
        self.sim2.set_pixel_at(p2pos, self.p2Color)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.A:
            self.raceState.advance_a()

        if key == arcade.key.B:
            self.raceState.advance_b()

        if key == arcade.key.KEY_0:
            self.raceState.reset()

        if key == arcade.key.KEY_1:
            self.raceState.start()

        if key == arcade.key.KEY_2:
            self.sim1.set_all((0, 255, 255, 255))
            self.sim2.set_all((0, 255, 255, 255))

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.hue += 0.01
        if self.hue >= 1.0:
            self.hue = self.hue - 1.0
        self.test_colour = ColorUtils.hsv_to_rgb_256(self.hue, 1, 1)

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()