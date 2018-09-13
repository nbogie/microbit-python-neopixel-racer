from microbit import *
import radio

# Fake Listener - pretends to be a race, and listens.
# 
# User selects group with button_a, then locks it in with button_b
# Then the device will show received messages on that group.
# Pro-tip:
# Hold button_b during power on to switch straight to group 21.

radio.on()

picking_group = True

display.scroll('Ear', 80)
if button_b.is_pressed():
    group = 21
    display.scroll('Pro')
    picking_group = False
else:
    group = 1

x = button_b.was_pressed()   # clear this flag

sleep(1000)
display.scroll(group, 60)

while picking_group:
    if button_a.was_pressed():
        group = group + 1
        display.scroll(group, 60)
    if button_b.was_pressed():
        picking_group = False

display.show(">")
display.clear()

radio.config(group=group)

sleep(1000)
display.scroll(group)

indicator = False

def toggle_indicator():
    global indicator
    display.set_pixel(0, 0, 8 if indicator else 0)
    indicator = not indicator
    
while True:
    incoming = radio.receive()
    if incoming is None:
        pass
    else:
        if incoming == 'a':
            display.show('a')
        elif incoming == 'b':
            display.show('b')
        elif incoming == 'start':
            display.show('s')
        # display.scroll(incoming, 50)
        toggle_indicator()
    sleep(10)