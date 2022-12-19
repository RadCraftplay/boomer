from abc import ABC, abstractmethod
import io
import json
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import pyttsx3

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

class SpeakingIOProvider(IOProvider):
    def __init__(self):
        def set_voice(engine : pyttsx3.Engine, language: str):
            for voice in engine.getProperty('voices'):
                id : str = voice.id
                if id.__contains__(language):
                    engine.setProperty("voice", voice.id)
                    break
            assert "Language not found!"

        self.engine = pyttsx3.init()
        set_voice(self.engine, "EN-US")
        self.engine.setProperty("rate", 160)
        
    def read(self) -> str:
        return input("> ")

    def write(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()