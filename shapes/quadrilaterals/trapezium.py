from typing import List
from shapes.quadrilaterals.quadrilateral import Quadrilateral


class Trapezium(Quadrilateral):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Trapezium"