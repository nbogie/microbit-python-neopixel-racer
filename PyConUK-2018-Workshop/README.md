# Adding sound and remote control to the micro:bit NeoPixelRacer!
## A PyCon UK 2018 Young Coders Day Workshop

Here are some resources from the PyCon UK 2018 Young Coders Day workshop called 
"Adding sound and remote control to the micro:bit NeoPixelRacer!"

## What's it about?

[Here's the original workshop description](https://2018.hq.pyconuk.org/schedule/item/E70D/):

"In this workshop we will add sound effects, music, and remote-controllers to an existing, exciting two-player neopixel light-racing game! 
We'll do this by using radio messaging between micro:bits, and we'll code this in MicroPython (It looks just like Python 3 code).

We'll make and customise the controllers ourselves.

If you're looking for cool project ideas for your micro:bit, you should definitely check this out!

Note: to get the most out of this workshop it is best if you've done a little bit of Python (or MicroPython) before. However, you do NOT need any experience with the micro:bit!

Note: We won't be programming the actual NeoPixels in this workshop, but we have made [the code for that part available](../src/) for anyone to reuse and learn from."

## What hardware and software did we use?

* We used little microcontrollers which are called [BBC micro:bits](https://microbit.org/).  Each Young Coder attending the Education Summit received one.

* We programmed them using [MicroPython](https://microbit-micropython.readthedocs.io/en/latest/) using a [free editor and uploader called Mu](https://codewith.mu/)

* The core of the race game was another microbit talking to 2 x 2metre strips of colourful "WS2812B" RGB LEDs, aka "NeoPixels".  
[The code used by that microbit is here](../src/RacerCore.py) however, for various reasons, that is not good code to learn from.
(NeoPixel is a brand name of these by the company [Adafruit](https://www.adafruit.com/?q=neopixels).)

## Tell me more about the LEDs used for your race tracks

The specific ones used in the workshop were rated 5v, and had a density of 30 LEDs per metre.

They were bought [here on amazon](https://www.amazon.co.uk/gp/product/B07C2QS663) when they cost £15 for a 5 metre strip (The price from that seller has since gone up).  Strips can be cut, though you'll need to do a small simple soldering job to re-attach 3 wires when you cut the strip.
To get the best price (but not necessarily a reliable product) many people would order such things directly from China via [ebay](https://www.ebay.co.uk/sch/i.html?_nkw=rgb+led+strip+5v+5m), [banggood](https://www.banggood.com/search/rgb-led-5v-5m-strip.html) or [aliexpress](https://www.aliexpress.com/wholesale?catId=0&SearchText=5v+rgb+led+strip+5m), hope for the best, and wait a month or so.

The LEDs were powered separately using a 4.5v battery pack.  It's important not to make any circuit (accidental or otherwise) from this pack to the microbit.  The microbit had a data line connected to the LEDs, and it also shared the common reference ("Ground") with them, but again, it's very important NOT to connect it to the 5v line from the battery pack or from the LED strips, as that will likely fry your microbit.

## How do I get started programming NeoPixels with micro:bit

For your first NeoPixel projects on micro:bit, I'd strongly recommend [Kitronik's Zip Halo](https://www.kitronik.co.uk/5625-zip-halo-for-the-bbc-microbit.html), assuming its circular form is suitable for you, and assuming you don't need to get access to the other pins on the microbit to connect to other hardware.  You'll need to get the correct battery pack with it.  (I'm not affiliated with Kitronik. They're great.)

An excellent guide all about NeoPixels is the [Adafruit NeoPixel Uberguide](https://learn.adafruit.com/adafruit-neopixel-uberguide/).

## MicroPython Documentation

Radio docs
* [Radio API docs](https://microbit-micropython.readthedocs.io/en/latest/radio.html)... 
and [radio tutorial](https://microbit-micropython.readthedocs.io/en/latest/tutorials/radio.html)

Music docs
* [Music API docs](https://microbit-micropython.readthedocs.io/en/latest/music.html)... 
and [music tutorial](https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html)

Text-to-Speech docs
 * [Text-to-Speech API docs](https://microbit-micropython.readthedocs.io/en/latest/tutorials/speech.html)... 
 and [Text-to-Speech tutorial](https://microbit-micropython.readthedocs.io/en/latest/tutorials/speech.html)
