"""
test circle class
"""
from pyturtle.shapes.circle import Circle

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
def test_circle_draw():
    turtle = TurtleMock()
    circle = Circle(turtle=turtle)
    circle.draw()

