from microbit import *
import radio

# Fake Sender - pretends to be a race.
# 
# User selects group with button_a, then locks it in with button_b
# Then selects message with button_a and sends it with button_b, (can repeat)
# Pro-tip:
# Hold button_b during power on to switch straight to group 21.

radio.on()

messages = ["init", 
            "p1moved", 
            "p2moved", 
            "red", 
            "amber", 
            "green", 
            "go", 
            "p1lead", 
            "p2lead", 
            "tied", 
            "p1won", 
            "p2won"]

msg_ix = 0

display.scroll('Fake')
if button_b.is_pressed():
    group = 21
    display.scroll('Pro')
else:
    group = 1

x = button_b.was_pressed()   # clear this flag

def get_msg():
    return messages[msg_ix]

sleep(1000)
display.scroll(group, 60)

picking_group = True
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


display.scroll(get_msg(), 70)
while True:
    if button_a.was_pressed():
        msg_ix = (msg_ix + 1) % len(messages)
        radio.send(get_msg())
        display.scroll(get_msg(), 70)
    if button_b.was_pressed():
        radio.send(get_msg())
        display.scroll(get_msg(), 70)
    sleep(10)