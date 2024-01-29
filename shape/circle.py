from math import pi

from shape.shape import Shape


class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y)
        self._radius = radius

    def calculate_area(self) -> float:
        return pi * self._radius ** 2

    def __str__(self) -> str:
        return f'circle(center=({self._x},{self._y}),radius={self._radius})'
