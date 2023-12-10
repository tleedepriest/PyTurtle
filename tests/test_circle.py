"""
test circle class
"""

from pyturtle.shapes.circle import Circle
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
   print('no display found. Using non-interactive Agg backend')
   mpl.use('Agg')
import matplotlib.pyplot as plt

def test_circle_draw():
    circle = Circle()
    circle.draw()

