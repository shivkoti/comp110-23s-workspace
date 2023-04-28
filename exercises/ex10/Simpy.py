"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "7350556602"


class Simpy:
    """Class Simpy."""

    values: list[float] = []

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Initialize the values attribute."""
        self.values = values

    def __str__(self) -> str:
        """Convert value into a string."""
        return f"Simpy({self.values})"
    
    def fill(self, elem: float, n: int) -> None:
        """Fill Simpy's values with a number of repeating values."""
        self.values = []
        i = 0
        while i < n:
            self.values.append(elem)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        assert step != 0.0
        if start <= 0:
            while start > stop:
                self.values.append(start)
                start += step
        while start < stop:
            self.values.append(start)
            start += step
    
    def sum(self) -> float: 
        """Compute sum for all items in values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add ability to use the + operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for elem in self.values:
                result.values.append(elem + rhs)
        else:
            i: int = 0
            while i < len(self.values): 
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add ability to use the ** operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for elem in self.values:
                result.values.append(elem ** rhs)
        else:
            i: int = 0
            while i < len(self.values): 
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add ability to use the == operator."""
        result = Simpy([])
        if isinstance(rhs, float):
            for elem in self.values:
                result.values.append(elem == rhs)
        else:
            i: int = 0
            while i < len(self.values): 
                result.values.append(self.values[i] == rhs.values[i])
                i += 1
        return result.values

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add ability to use the > operator."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for elem in self.values:
                result.values.append(elem > rhs)
        else:
            i: int = 0
            while i < len(self.values): 
                result.values.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add subscription notation support."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
        return result
