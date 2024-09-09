import pytest
import numpy as np
from pyturtle.shapes.arc import Arc
from pyturtle.shapes.point import Point2D

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


def test_arc():
    # from turtle import Turtle
    # Create an instance of Line
    #turtle = TurtleMock()
    arc = Arc()
    # Call the draw method
    assert arc.radius == 10
    assert len(arc.coordinates) == 0
    arc.set_coordinates()
    assert len(arc.coordinates) == 100
    assert arc.center == Point2D(0, 0)
    assert arc.coordinates[0] == Point2D(10, 0) # default radius 10
    arc.translate_x(10)
    assert arc.center == Point2D(10, 0)
    arc.translate_y(10)
    assert arc.center == Point2D(10, 10)
    arc.translate_xy(10, 10)
    assert arc.center == Point2D(20, 20)
    new_arc = Arc()
    assert new_arc.center == Point2D(0, 0)