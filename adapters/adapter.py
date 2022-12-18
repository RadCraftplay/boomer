from abc import ABC, abstractmethod
from typing import Callable


class Adapter(ABC):
    @abstractmethod
    def can_parse(self, sentence: str) -> tuple[bool, float]:
        pass

    @abstractmethod
    def get_response(self, sentence: str) -> Callable[[], str]:
        pass