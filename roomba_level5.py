# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Oakrimed
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves)

###
# Start your code here
forward(40)
right(90)
backward(40)
forward(80)
left(90)
forward(40)
right(90)
forward(40)
backward(160)
forward(40)
left(90)
forward(40)
right(90)
forward(80)
backward(40)
left(90)
forward(80)
right(90)
forward(120)
backward(120)
for i in range(3):
  left(90)
  forward(40)
  right(90)
  forward(160)
  backward(160)
left(90)
forward(40)
right(90)
forward(360)
right(180)

forward(40)
right(90)
backward(40)
forward(80)
left(90)
forward(40)
right(90)
forward(40)
backward(160)
forward(40)
left(90)
forward(40)
right(90)
forward(80)
backward(40)
left(90)
forward(80)
right(90)
forward(120)
backward(120)
for i in range(3):
  left(90)
  forward(40)
  right(90)
  forward(160)
  backward(160)
left(90)
forward(40)
right(90)
forward(200)

right(180)
forward(40)
right(90)
forward(120)
backward(120)
for i in range(3):
  left(90)
  forward(40)
  right(90)
  forward(160)
  backward(160)
left(90)
forward(40)
right(90)
forward(360)
right(180)

forward(40)
right(90)
backward(40)
forward(80)
left(90)
forward(40)
right(90)
forward(40)
backward(160)
forward(40)
left(90)
forward(40)
right(90)
forward(80)
backward(40)
left(90)
forward(80)
right(90)
forward(120)
backward(120)
for i in range(3):
  left(90)
  forward(40)
  right(90)
  forward(160)
  backward(160)
left(90)
forward(40)
right(90)
forward(360)
right(180)
# End your code here
###
 
window.exitonclick()