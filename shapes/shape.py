from typing import List


class Shape:
    name: str
    sides: List[float]

    def __init__(self, sides: List[float]) -> None:
        self.sides = sides

    def area(self) -> float:
        """
        Calculates the area of the shape
        """
        raise NotImplementedError

    def interior_angle(self) -> float:
        """
        Calculates the interior angle of the shape
        """
        return (len(self.sides) - 2) * 180 / len(self.sides)

    def print_stats(self) -> str:
        return f"Name: {self.name}\nArea: {self.area()}\nInterior Angle: {self.interior_angle()}"
