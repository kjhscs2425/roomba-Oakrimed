# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Oakrimed
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3)

###
# Start your code here
for i in range(4):
  forward(40)
  right(90)
  forward(120)
  left(90)
  forward(40)
  right(90)
  backward(200)
  forward(240)
  left(90)
  forward(120)
  left(90)
  backward(40)
forward(120)
right(90)
forward(80)
backward(160)
left(90)
forward(40)
right(90)
for j in range(2):
  forward(160)
  left(90)
  forward (40)
  left(90)
  forward(160)
  right(90)
  forward (40)
  right(90) 
# End your code here
###
 
window.exitonclick()