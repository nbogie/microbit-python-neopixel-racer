__all__ = ['NeoPixel'
           ]


class NeoPixel:
    def __init__(self, pin, num_pixels):
        self.pin = pin
        self.num_pixels = num_pixels
        self.buffer = [0] * num_pixels

    def show(self):
        pass

    def clear(self):
        pass

    def __setitem__(self, ix, color): self.buffer[ix] = color











