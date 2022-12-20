import unittest

from typing import Union
from functools import partial

Heading = Union[str, "N", "W", "S", "E"]
Coordinates = (int, int)
COMPASS: list[Heading] = ["N", "E", "S", "W"]


def rotate(turns: int) -> Heading:
    def heading(heading: Heading) -> Heading:
        idx = COMPASS.index(heading)
        return COMPASS[(idx + turns) % 4]
    return heading


turn_left = partial(rotate(3))
turn_right = partial(rotate(1))


def move(heading: Heading, position: Coordinates) -> Coordinates:
    x, y = position
    match heading:
        case "N": return x, y + 1
        case "E": return x + 1, y
        case "S": return x, y - 1
        case "W": return x - 1, y


class MainTest(unittest.TestCase):
    def test_turn_left(self):
        # when facing N, turning left should case us to face W
        self.assertEqual(turn_left("N"), "W")

        # when facing W, turning left should case us to face S
        self.assertEqual(turn_left("W"), "S")

        # when facing R, turning left should case us to face E
        self.assertEqual(turn_left("S"), "E")

        # when facing E, turning left should case us to face N
        self.assertEqual(turn_left("E"), "N")

    def test_turn_right(self):
        # when facing N, turning left should case us to face E
        self.assertEqual(turn_right("N"), "E")

        # when facing E, turning left should case us to face S
        self.assertEqual(turn_right("E"), "S")

        # when facing S, turning left should case us to face W
        self.assertEqual(turn_right("S"), "W")

        # when facing W, turning left should case us to face N
        self.assertEqual(turn_right("W"), "N")

    def test_moves(self):
        # when moving N, we sould increment the Y coordinate
        self.assertEqual(move("N", (1, 1)), (1, 2))

        # when moving E, we should increment the X coordinate
        self.assertEqual(move("E", (1, 1)), (2, 1))

        # when moving S, we should decrement the X coordinate
        self.assertEqual(move("S", (1, 1)), (1, 0))

        # when moving W, we should decrement the X coordinate
        self.assertEqual(move("W", (1, 1)), (0, 1))


if __name__ == "__main__":
    unittest.main()

