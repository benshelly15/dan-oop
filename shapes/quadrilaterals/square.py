from typing import List
from shapes.quadrilaterals.quadrilateral import Quadrilateral


class Square(Quadrilateral):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Square"