#!/usr/bin/env python3

# This is how we load a library in Python
from ev3dev2.sound import Sound

# By the way, this is a comment! Comments are often used to explain how the code
# works. There is some code below that you can uncomment by removing the "#" 
# characters.

# "Sound" is a "class". It's a type of thing.
# We're now going to create an "instance" (or a thing).
sound = Sound()

# And now we're going to call a "method" on the instance.
# What do you think this does? Can you make it say your name?
# Hint: Press the "F5" key in Visual Studio Code to run the program.
sound.speak('Hello there')

#
# What other things would you expect to do with a sound instance?
# How about:
#

## .. set the volume (100 is the loudest)  
#sound.set_volume(50)

## ... play a beep?
#sound.beep()

## ... play a sound from a file (can you see another sound file on the left?)
#sound.play('elephant.wav')

## ... play a song? All of the lines below need to be uncommented.
#sound.play_song((
#    ('A2', 'q'), 
#    ('A2', 'q'),
#    ('A2', 'q'),
#    ('F2', 'q/2'),
#    ('C3', 'q/3'),
#    ('A2', 'q'),
#    ('F2', 'q/2'),
#    ('C3', 'q/3'),
#    ('A2', 'q')))
