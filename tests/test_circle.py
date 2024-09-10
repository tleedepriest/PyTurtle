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
    circle = Circle()
    circle.set_coordinates()
    circle.draw(turtle_instance=turtle)


def test_circle_translate_x():
    one = Circle()
    one.set_coordinates()
    coords = one.get_coordinates()
    one.translate_x(10)
    coords_shifted = one.get_coordinates()
    assert len(coords) == len(coords_shifted)
    for i in range(len(coords)):
        assert coords[i].y == coords_shifted[i].y
        assert coords[i].x != coords_shifted[i].x


def test_circle_translate_y():
    one = Circle()
    one.set_coordinates()
    coords = one.get_coordinates()
    one.translate_y(10)
    coords_shifted = one.get_coordinates()
    assert len(coords) == len(coords_shifted)
    for i in range(len(coords)):
        assert coords[i].y != coords_shifted[i].y
        assert coords[i].x == coords_shifted[i].x


def test_circle_rotate():
    one = Circle()
    one.set_coordinates()
    coords = one.get_coordinates()
    one.rotate(angle=45)
    coords_rotated = one.get_coordinates()
    assert len(coords) == len(coords_rotated)
    for i in range(len(coords)):
        assert coords[i].y != coords_rotated[i].y
        assert coords[i].x != coords_rotated[i].x


def test_circle_rotate_360():
    one = Circle()
    one.set_coordinates()
    coords = one.get_coordinates()
    one.rotate(angle=360)
    coords_rotated = one.get_coordinates()
    assert len(coords) == len(coords_rotated)
    for i in range(len(coords)):
        assert coords[i].y == coords_rotated[i].y
        assert coords[i].x == coords_rotated[i].x


def test_circle_rotate_0():
    one = Circle()
    one.set_coordinates()
    coords = one.get_coordinates()
    one.rotate(angle=0)
    coords_rotated = one.get_coordinates()
    assert len(coords) == len(coords_rotated)
    for i in range(len(coords)):
        assert coords[i].y == coords_rotated[i].y
        assert coords[i].x == coords_rotated[i].x
