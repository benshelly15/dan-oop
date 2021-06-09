from typing import List
from shapes.quadrilaterals.quadrilateral import Quadrilateral


class Kite(Quadrilateral):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Kite"