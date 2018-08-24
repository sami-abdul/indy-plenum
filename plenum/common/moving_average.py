import math
from abc import ABC, abstractmethod


class MovingAverage(ABC):
    @abstractmethod
    def update(self, value: float):
        pass

    @property
    @abstractmethod
    def value(self) -> float:
        return self._value


class ExponentialMovingAverage(MovingAverage):
    def __init__(self, start: float, alpha: float):
        self._value = start
        self._alpha = alpha

    def update(self, value: float):
        self._value = value * self._alpha + self._value * (1 - self._alpha)

    @property
    def value(self) -> float:
        return self._value

    @staticmethod
    def halfway_alpha(steps):
        return -math.log(0.5) / steps
