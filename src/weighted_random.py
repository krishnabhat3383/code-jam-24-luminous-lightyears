import random
from typing import Any, Generic, Protocol, TypeVar


class SupportsWeight(Protocol):
    @property
    def weight(self) -> int: ...


T = TypeVar("T", bound=SupportsWeight)


class WeightedList(Generic[T]):
    def __init__(self, values: list[T] | None = None) -> None:
        if values is not None:
            self.values = values
            self.weights = [value.weight for value in values]
        else:
            self.values = []

    def append(self, value: T) -> None:
        self.values.append(value)
        self.weights.append(value.weight)

    def get_random(self) -> T:
        return random.choices(self.values, weights=self.weights, k=1)[0]  # noqa: S311 Not for cryptographic purposes
