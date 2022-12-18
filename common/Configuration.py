
from abc import ABC, abstractmethod
import json
from os.path import exists


class ConfigurationProvider(ABC):
    @abstractmethod
    def read(self):
        pass

class JsonConfigurationProvider(ConfigurationProvider):

    def __init__(self, path: str) -> None:
        self.path = path

    def read(self):
        if not exists(self.path):
            assert "ERROR: Configuration file does not exist!"
        
        with open(self.path) as file:
            return json.load(file)