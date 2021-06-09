from typing import List
from shapes.triangles.triangle import Triangle


class RightAngled(Triangle):
    def __init__(self, sides: List[float]) -> None:
        super().__init__(sides)
        self.name = "Right Angled Triangle"