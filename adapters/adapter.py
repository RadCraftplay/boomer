from abc import ABC, abstractmethod


class Adapter(ABC):
    @abstractmethod
    def can_parse(self, sentence: str):
        pass

    @abstractmethod
    def get_response(self, sentence: str) -> str:
        pass