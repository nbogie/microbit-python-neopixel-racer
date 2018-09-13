# microbit-python-neopixel-racer
What is it?  This is a micropython implementation of my BBC microbit modular neopixel racer system.

## Installation:
* install race core, and connect to neopixels - it may be necessary to install using Mu's "minify before flashing" micro:bit setting.
Optionally install the following, for full system demo, but ideally have the students design and build their own and more.
* install sample sfx onto a microbit with headphones/speaker
* install sample speech sfx onto a microbit with headphones/speaker
* install sample touch or button controller onto one or more microbits with relevant cardboard circuitry.
* install sample servo "position indicator" onto a microbit with a servo on pin 1.

## Issues:

What's more difficult about the MicroPython implementation than the MakeCode / Javascript one?

* Less space for code.  The micro:bit is running out of memory with what i'd like to implement, even with Mu's "minify before flashing" micro:bit setting.  So some features from the original have been thrown overboard (such as user-chosen colours and fancier animations).
* max depth of around 8 nested calls: https://mail.python.org/pipermail/microbit/2016-February/000896.html
* There's no RGBW neopixel support (my existing hardware was RGBW, which is supported in makecode/javascript).
* There's no simulator

Pros:

* REPL
* The students get to use (Micro)Python

## misc resources

* https://microbit-micropython.readthedocs.io/en/latest/radio.html
* https://microbit-micropython.readthedocs.io/en/latest/music.html
* https://microbit-micropython.readthedocs.io/en/latest/tutorials/speech.html

* on call depth (memory) issues: https://mail.python.org/pipermail/microbit/2016-February/000896.html
* on radio comms between makecode and micropython: TODO
