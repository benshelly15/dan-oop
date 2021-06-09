from typing import List
from math import sqrt
from shapes.shape import Shape


class Hexagon(Shape):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Hexagon"

    def area(self) -> float:
        return (3*sqrt(3)/2)*self.sides[0]**2