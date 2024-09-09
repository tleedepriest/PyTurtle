import pytest
from pyturtle.shapes.line import Line

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


def test_line():
    # Create an instance of Line
    turtle = TurtleMock()
    #steps = 10
    start = (0, 0)
    end = (100, 100)
    line = Line(start=start, end=end)
    line.set_coordinates()
    # Call the draw method
    assert line.start.x == 0
    assert line.start.y == 0
    assert line.end.x == 100
    assert line.end.y == 100
    line.translate_x(10)
    assert line.start.x == 10
    assert line.start.y == 0
    
    assert line.end.x == 110
    assert line.end.y == 100

    line.translate_y(10)
    assert line.start.x == 10
    assert line.start.y == 10

    assert line.end.x == 110
    assert line.end.y == 110

    line.draw(turtle_instance=turtle)

    # Assertions
    #assert turtle.penup_called
    #assert turtle.pendown_called
    #assert (x1, y1) in turtle.goto_called_with
    #assert (x2, y2) in turtle.goto_called_with
    assert len(line.coordinates) == 2
