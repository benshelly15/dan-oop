from shapes.quadrilaterals.square import Square
from shapes.triangles.scalene import Scalene
from shapes.triangles.isosceles import Isoscles
from shapes.triangles.right_angled import RightAngled
from shapes.triangles.equilateral import Equilateral
from shapes.hexagon import Hexagon
from shapes.pentagon import Pentagon
from shapes.quadrilaterals.quadrilateral import Quadrilateral
from shapes.triangles.triangle import Triangle
from shapes.shape import Shape
from typing import List


class ShapeFactory:
    def __init__(self, sides: List[float]) -> None:
        self.sides = sides
        
    def create(self) -> Shape:
        """
        Creates a Shape from the given sides
        """
        if (len(self.sides) == 3):
            return self._create_triangle()
        elif (len(self.sides) == 4):
            return self._create_quadrilateral()
        elif (len(self.sides) == 5):
            return Pentagon(self.sides)
        elif (len(self.sides) == 6):
            return Hexagon(self.sides)
        else:
            raise RuntimeError("This program only supports 3 - 6 sided shapes")

    def _create_triangle(self) -> Triangle:
        """
        Creates a triangle
        """
        if (self._all_equal()):
            return Equilateral(self.sides)
        angles = Triangle.get_angles(self.sides)
        if 90.0 in angles:
            return RightAngled(self.sides)
        elif (angles[0] == angles[1] or angles[0] == angles[2] or angles[1] == angles[2]):
            return Isoscles(self.sides)
        else:
            return Scalene(self.sides)

    def _create_quadrilateral(self) -> Quadrilateral:
        """
        Creates a quadrilateral
        """
        if (self._all_equal()):
            return Square(self.sides)

    def _all_equal(self):
        """
        Returns true if all elements in list are equal
        """
        iterator = iter(self.sides)
        try:
            first = next(iterator)
        except StopIteration:
            return True
        return all(first == x for x in iterator)
