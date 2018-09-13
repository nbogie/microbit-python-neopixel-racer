let lastPixelNumber = 0
let numPixels = 0
let movementStep = 0
let winnerColour = 0
let p2Colour = 0
let loserStrip: neopixel.Strip = null
let p2Pos = 0
let p1Colour = 0
let raceDuration = 0
let defaultBrightness = 0
let strip2: neopixel.Strip = null
let strip1: neopixel.Strip = null
let winnerStrip: neopixel.Strip = null
let p1Pos = 0
let raceStartTime = 0
let winnerId = 0
let p1Hue = 0
let p2Hue = 0
let raceState = ""
let trafficLightColour = 0


function showPlayer2()  {
    strip2.setBrightness(defaultBrightness)
    strip2.clear()
    strip2.setPixelColor(p2Pos, neopixel.hsl(p2Hue, 99, 50))
    if (p2Pos >= 1) {
        strip2.setPixelColor(p2Pos - 1, neopixel.hsl(p2Hue, 99, 8))
    }
    if (p2Pos >= 2) {
        strip2.setPixelColor(p2Pos - 2, neopixel.hsl(p2Hue, 99, 2))
    }
    strip2.show()
}
input.onPinPressed(TouchPin.P2, () => {
    p1Pressed()
})
function startCountdown()  {
    raceState = "countdown"
    radio.sendNumber(10)
    basic.pause(1000)
    strip1.setBrightness(defaultBrightness)
    strip2.setBrightness(defaultBrightness)
    trafficLightColour = NeoPixelColors.Red
    pulseTrafficLight()
    radio.sendNumber(11)
    basic.pause(1000)
    trafficLightColour = NeoPixelColors.Orange
    pulseTrafficLight()
    radio.sendNumber(12)
    basic.pause(1000)
    trafficLightColour = NeoPixelColors.Green
    pulseTrafficLight()
    radio.sendNumber(13)
    basic.pause(1000)
    radio.sendNumber(20)
    raceStarted()
}
function cycleP2Hue()  {
    p2Hue += 2
    if (p2Hue >= 360) {
        p2Hue = 0
    }
}
function raceStarted()  {
    raceState = "running"
    raceStartTime = input.runningTime()
    p1Pos = 1
    p2Pos = 1
    showPlayer1()
    showPlayer2()
}
function choosingColours()  {
    raceState = "choosingColours"
    p1Pos = 0
    p2Pos = 0
    radio.sendNumber(5)
    showPlayer1()
    showPlayer2()
}
input.onGesture(Gesture.Shake, () => {
    radio.sendNumber(130)
    startRacePressed()
})
function cycleP1Hue()  {
    p1Hue += 2
    if (p1Hue >= 360) {
        p1Hue = 0
    }
}
input.onButtonPressed(Button.A, () => {
    p1Pressed()
})
function winAsP2()  {
    winnerId = 2
    winnerStrip = strip2
    loserStrip = strip1
    winnerColour = p2Colour
    radio.sendNumber(32)
    winRace()
}
function pulseTrafficLight()  {
    strip1.clear()
    strip2.clear()
    for (let index = 0; index <= numPixels / 3; index++) {
        strip1.setPixelColor(numPixels / 2 - index, trafficLightColour)
        strip1.setPixelColor(numPixels / 2 + index, trafficLightColour)
        strip1.show()
        strip2.setPixelColor(numPixels / 2 - index, trafficLightColour)
        strip2.setPixelColor(numPixels / 2 + index, trafficLightColour)
        strip2.show()
        // buggy library RGBW impl with ranges?
        // strip1.range(numPixels / 2 - index, 2 *
        // index).showColor(trafficLightColour)
        // strip2.range(numPixels / 2 - index, 2 *
        // index).showColor(trafficLightColour)
        basic.pause(2)
    }
}
function handleChangingColoursFrame()  {
    if (input.buttonIsPressed(Button.A)) {
        cycleP1Hue()
        p1Colour = neopixel.hsl(p1Hue, 99, 50)
        showPlayer1()
    }
    if (input.buttonIsPressed(Button.B)) {
        cycleP2Hue()
        p2Colour = neopixel.hsl(p2Hue, 99, 50)
        showPlayer2()
    }
    if (input.pinIsPressed(TouchPin.P2)) {
        startRacePressed()
    }
}
function showPlayer1()  {
    strip1.setBrightness(defaultBrightness)
    strip1.clear()
    strip1.setPixelColor(p1Pos, neopixel.hsl(p1Hue, 99, 50))
    if (p1Pos >= 1) {
        strip1.setPixelColor(p1Pos - 1, neopixel.hsl(p1Hue, 99, 8))
    }
    if (p1Pos >= 2) {
        strip1.setPixelColor(p1Pos - 2, neopixel.hsl(p1Hue, 99, 2))
    }
    strip1.show()
}
function announceLeader()  {
    if (p1Pos > p2Pos) {
        radio.sendNumber(21)
    } else if (p1Pos < p2Pos) {
        radio.sendNumber(22)
    } else {
        radio.sendNumber(23)
    }
}
input.onButtonPressed(Button.B, () => {
    p2Pressed()
})
function runEndOfRaceAnims()  {
    winnerStrip.setBrightness(defaultBrightness)
    loserStrip.setBrightness(defaultBrightness)
    loserStrip.clear()
    loserStrip.show()
    winnerStrip.clear()
    winnerStrip.show()
    for (let ix3 = 0; ix3 <= numPixels - 1; ix3++) {
        winnerStrip.setPixelColor(ix3, winnerColour)
        winnerStrip.show()
        basic.pause(10)
    }
    for (let ix4 = 0; ix4 <= numPixels - 2 - 1; ix4++) {
        loserStrip.setPixelColor(numPixels - ix4, winnerColour)
        loserStrip.show()
        basic.pause(10)
    }
    for (let i = 0; i < numPixels - 1; i++) {
        loserStrip.shift(1)
        loserStrip.show()
        winnerStrip.shift(1)
        winnerStrip.show()
        basic.pause(1)
    }
    choosingColours()
}
function startRacePressed()  {
    if (raceState == "choosingColours") {
        startCountdown()
    }
}
radio.onDataPacketReceived( ({ receivedNumber }) =>  {
    if (receivedNumber == 101) {
        p1Pressed()
    } else if (receivedNumber == 102) {
        p2Pressed()
    } else if (receivedNumber == 130) {
        startRacePressed()
    } else {
    	
    }
})
function p2Pressed()  {
    if (raceState == "running") {
        radio.sendNumber(2)
        p2Pos += movementStep
        showPlayer2()
        if (p2Pos >= lastPixelNumber) {
            winAsP2()
        } else {
            announceLeader()
        }
    } else if (raceState == "choosingColours") {
        for (let i = 0; i < 5; i++) {
            cycleP2Hue()
        }
        led.toggle(4, 0)
        showPlayer2()
    } else {
        radio.sendNumber(102)
    }
}
function p1Pressed()  {
    if (raceState == "running") {
        radio.sendNumber(1)
        p1Pos += movementStep
        showPlayer1()
        if (p1Pos >= lastPixelNumber) {
            winAsP1()
        } else {
            announceLeader()
        }
    } else if (raceState == "choosingColours") {
        for (let i = 0; i < 5; i++) {
            cycleP1Hue()
        }
        led.toggle(0, 0)
        showPlayer1()
    } else {
        radio.sendNumber(201)
    }
}
function winAsP1()  {
    winnerId = 1
    winnerStrip = strip1
    loserStrip = strip2
    winnerColour = p1Colour
    radio.sendNumber(31)
    winRace()
}
function winRace()  {
    raceState = "ended"
    raceDuration = input.runningTime() - raceStartTime
    runEndOfRaceAnims()
}


raceState = "uninit"
radio.setGroup(21)
movementStep = 1
numPixels = 60
lastPixelNumber = numPixels - 1
p1Hue = Math.random(360)
p2Hue = Math.random(360)
defaultBrightness = 200
p1Pos = 0
p2Pos = 0
p1Colour = neopixel.hsl(p1Hue, 99, 50)
p2Colour = neopixel.hsl(p2Hue, 99, 50)
trafficLightColour = NeoPixelColors.Red
strip1 = neopixel.create(DigitalPin.P0, numPixels, NeoPixelMode.RGBW)
strip2 = neopixel.create(DigitalPin.P1, numPixels, NeoPixelMode.RGBW)
raceDuration = 0
radio.sendNumber(0)
strip1.setPixelColor(p1Pos, p1Colour)
strip1.show()
strip2.setPixelColor(p2Pos, p2Colour)
strip2.show()
basic.pause(500)
if (input.buttonIsPressed(Button.B)) {
    basic.showString("P0+1:LEDs", 50)
}
choosingColours()
basic.showString("*race2p ch21", 50)
basic.forever(() => {
    if (raceState == "running") {
        basic.pause(90)
    } else {
        if (raceState == "choosingColours") {
            handleChangingColoursFrame()
            basic.pause(10)
        } else {
        	
        }
    }
    basic.pause(10)
})