from typing import List
from math import sqrt
from shapes.shape import Shape


class Quadrilateral(Shape):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)

    def area(self) -> float:
        semiperimeter = sum(self.sides) / 2
        return sqrt((semiperimeter - self.sides[0]) *
                    (semiperimeter - self.sides[0]) *
                    (semiperimeter - self.sides[0]) *
                    (semiperimeter - self.sides[0]))