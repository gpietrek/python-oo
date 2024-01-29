from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def __str__(self):
        pass
