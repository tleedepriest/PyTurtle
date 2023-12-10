import pytest
import numpy as np
from pyturtle.shapes.arc import Arc
from pyturtle.shapes.point import Point2D
import os
import matplotlib as mpl

if os.environ.get('DISPLAY','') == '':
   print('no display found. Using non-interactive Agg backend')
   mpl.use('Agg')
import matplotlib.pyplot as plt

class TurtleMock:
    def __init__(self):
        self.penup_called = False
        self.pendown_called = False
        self.goto_called_with = []

    def penup(self):
        self.penup_called = True

    def pendown(self):
        self.pendown_called = True

    def goto(self, x, y):
        self.goto_called_with.append((x, y))


def test_arc_draw():
    # Create an instance of Line
    # turtle = TurtleMock()
    arc = Arc()
    # Call the draw method
    arc.draw()
    assert len(arc.coordinates) == 100
    print(arc.coordinates)
    assert arc.center == Point2D(0, 0)
    assert arc.coordinates[0] == Point2D(10, 0)
    arc.rotate(np.pi)
    print(arc.coordinates[0])
    assert arc.coordinates[0] == Point2D(-10, 0)
    arc.translate_x(10)
    arc.draw()
    # Assertions
    # assert turtle.penup_called
    # assert turtle.pendown_called
    assert arc.center == Point2D(10, 0)
    assert len(arc.coordinates) == 100
    arc.translate_y(10)
    arc.draw()
    assert arc.center == Point2D(10, 10)
    assert len(arc.coordinates) == 100
    arc.translate_xy(10, 10)
    assert arc.center == Point2D(20, 20)
    assert len(arc.coordinates) == 100
    arc.draw()
