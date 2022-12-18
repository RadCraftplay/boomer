from abc import ABC, abstractmethod

class IOProvider(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

    @abstractmethod
    def write(self, text: str):
        pass

class ConsoleIOProvider(IOProvider):
    def read(self) -> str:
        return input("> ")

    def write(self, text: str):
        print(text)