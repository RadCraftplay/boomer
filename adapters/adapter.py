
from abc import ABC, abstractmethod
from ast import Tuple


class Adapter(ABC):
    @abstractmethod
    def can_parse(sentence) -> Tuple[bool, float]:
        pass

    @abstractmethod
    def get_response(sentence) -> str:
        pass