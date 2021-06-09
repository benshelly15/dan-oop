from typing import List
from math import sqrt
from shapes.shape import Shape


class Pentagon(Shape):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Pentagon"

    def area(self) -> float:
        return 0.25*sqrt(5*(7*sqrt(5)))*self.sides[0]**2
