from random import random

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