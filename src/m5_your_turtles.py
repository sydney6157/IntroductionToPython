"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Sydney larson.
"""
########################################################################
# TODO: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

sam = rg.SimpleTurtle('turtle')
sam.pen = rg.Pen('midnight blue', 3)
sam.speed = 100  # Fast

john = rg.SimpleTurtle('turtle')
john.pen = rg.Pen('red', 3)
john.speed = 100  # Fast

radius = 100

for k in range(15):

    sam.draw_circle(radius)

    sam.pen_up()
    sam.right(60)
    sam.forward(20)
    sam.left(60)

    sam.pen_down()
    radius= radius - 12

rad = 100
for k in range(15):

    john.draw_circle(rad)

    john.pen_up()
    john.right(120)
    john.forward(20)
    john.left(120)

    john.pen_down()
    rad= rad - 12


window.close_on_mouse_click()
