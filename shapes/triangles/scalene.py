from typing import List
from shapes.triangles.triangle import Triangle


class Scalene(Triangle):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Scalene"