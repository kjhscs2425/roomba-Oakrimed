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

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
forward(40)
forward(520)
left(90)
forward(40)
left(90)
for i in range(9):
  forward(560)
  right(90)
  forward(40)
  right(90)
  forward(560)
  left(90)
  forward(40)
  left(90)
forward(560)
# End your code here
###
 
window.exitonclick()