#!/usr/bin/env python3

# This is how we load a library in Python
from ev3dev2.sound import Sound

# By the way, this is a comment!

# "Sound" is a "class". It's a type of thing.
# We're now going to create an "instance"
sound = Sound()

# And now we're going to call a "method" on the instance.
# What do you think this does?
sound.speak('Hello there')

#
# What other things would you expect to do with a sound instance?
#

## Set the volume (100 is the loudest)
sound.set_volume(50)

## play a beep?
# sound.beep()

## play a sound from a file
sound.play('elephant.wav')

## Play a song?
# sound.play_song((
#    ('A2', 'q'), 
#    ('A2', 'q'),
#    ('A2', 'q'),
#    ('F2', 'q/2'),
#    ('C3', 'q/3'),
#    ('A2', 'q'),
#    ('F2', 'q/2'),
#    ('C3', 'q/3'),
#    ('A2', 'q')))

