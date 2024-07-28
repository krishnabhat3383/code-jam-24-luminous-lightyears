"""Weight random list implementation."""

import random
from typing import TYPE_CHECKING, Generic, Protocol, TypeVar

if TYPE_CHECKING:
    from src.player import PlayerState


class SupportedRandomValue(Protocol):
    """Generic type for supported classes."""

    @property
    def weight(self) -> int: ...  # noqa: D102

    def is_available(self, state: "PlayerState") -> bool: ...  # noqa: D102


T = TypeVar("T", bound=SupportedRandomValue)


class WeightedList(Generic[T]):
    """Responsible for storing and retrieving values based on weights."""

    def __init__(self, values: list[T] | None = None) -> None:
        if values is not None:
            self.values = values
            self.weights = [value.weight for value in values]
        else:
            self.values = []
            self.weights = []

    def append(self, value: T) -> None:
        """Add a value to the weighted list."""
        self.values.append(value)
        self.weights.append(value.weight)

    def get_random(self, state: "PlayerState") -> T:
        """Get a random value based on the weights."""
        result = None

        if not self.values:
            return result

        while result is None:
            possible_result = random.choices(self.values, weights=self.weights, k=1)[0]

            if possible_result.is_available(state):
                result = possible_result

        return result
