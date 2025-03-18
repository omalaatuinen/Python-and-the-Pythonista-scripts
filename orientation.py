# This script is very useful, if You have a pythonista app. It returns one of 18 device (iphone or ipad) orientatio positions.
# Knowing the device orientation, You can program a different actions for each of 18 orientation positions. 
# It means, the one action button press can perform 18 different things depending on the device's orientation position.
# in the shortcuts app, add the "Run Pythonista script" action. In this action, tick the "Inline Script" checkbox.

import motion
import time
import json
import sys
import math


motion.start_updates()

time.sleep(0.02)

attitude = motion.get_attitude()

motion.stop_updates()

if attitude:
    roll = math.floor(math.degrees(attitude[0]))

    pitch = math.floor(math.degrees(attitude[1]))  
    
    yaw = math.floor(math.degrees(attitude[2]))

    def get_position(alpha, beta, pos=0):
      if 23 > alpha > -23 and 23 > beta > -23:
          pos = 1

      if 22 < alpha < 63 and 23 > beta > -23:
          pos = 2

      if alpha > 62:
          pos = 3

      if 22 < alpha < 63 and (beta < -136 or beta > 136):
          pos = 4

      if 23 > alpha > -23 and (beta < -158 or beta > 158):
          pos = 5

      if -22 > alpha > -61 and (beta < -136 or beta > 136):
          pos = 6

      if alpha < -60:
          pos = 7

      if -22 > alpha > -61 and (-23 < beta < 23):
          pos = 8

      if 23 > alpha > -23 and 22 < beta < 67:
          pos = 9

      if 23 > alpha > -23 and 66 < beta < 113:
          pos = 10

      if 23 > alpha > -23 and 112 < beta < 159:
          pos = 11

      if 23 > alpha > -23 and -22 > beta > -67:
          pos = 12

      if 23 > alpha > -23 and -66 > beta > -113:
          pos = 13

      if 23 > alpha > -23 and -112 > beta > -159:
          pos = 14

      if 63 > alpha > 22 and 125 > beta > 45:
          pos = 15

      if -22 > alpha > -61 and 125 > beta > 40:
          pos = 16

      if -22 > alpha > -61 and -45 > beta > -113:
          pos = 17

      if 63 > alpha > 22 and -40 > beta > -113:
          pos = 18

      return pos
    pos = get_position(pitch, roll)
    output = {
        "roll": roll,
        "pitch": pitch,
        "yaw": yaw,
        "pos": pos
    }

    sys.stdout.write(json.dumps(output))  
else:
    sys.stdout.write("No data")
# the device's orientation position is in the pos variable.
