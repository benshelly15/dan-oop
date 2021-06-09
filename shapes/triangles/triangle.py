from typing import List
from math import sqrt, acos
from shapes.shape import Shape


class Triangle(Shape):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)

    @staticmethod
    def get_angles(sides: List[float]) -> List[float]:
        angles = []
        angles[0] = acos(sides[1]**2 + sides[2]**2 - sides[0]**2)/2*sides[1]*sides[2]
        angles[1] = acos(sides[2]**2 + sides[0]**2 - sides[1]**2)/2*sides[2]*sides[0]
        angles[2] = 180 - angles[0] - angles[1]
        return angles

    def area(self) -> float:
        perimeter = sum(self.sides) / 2
        return sqrt(perimeter*(perimeter - self.sides[0])*(perimeter - self.sides[1])*(perimeter - self.sides[2]))