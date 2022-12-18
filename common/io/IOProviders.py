from abc import ABC, abstractmethod
import json
import speech_recognition as sr

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
    
class SpeechIOProvider(IOProvider):
    def __init__(self):    	
        pass

    def read(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        
        result = json.loads(r.recognize_vosk(audio))
        print(result)
        return result["text"]

    def write(self, text: str):
        print(text)