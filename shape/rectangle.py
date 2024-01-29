from shape.shape import Shape


class Rectangle(Shape):
    def __init__(self, x: float, y:float, width:float, height: float) -> None:
        super().__init__(x, y)
        self._width = width
        self._height = height

    def calculate_area(self) -> float:
        return self._width * self._height

    def __str__(self) -> str:
        return f'rectangle(center=({self._x},{self._y}),width={self._width},height={self._height})'
