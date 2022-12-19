from abc import ABC, abstractmethod
import json
import queue
import sys
import sounddevice as sd
import pyttsx3
from vosk import Model, KaldiRecognizer

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
        def set_voice(engine : pyttsx3.Engine, language: str):
            for voice in engine.getProperty('voices'):
                id : str = voice.id
                if id.__contains__(language):
                    engine.setProperty("voice", voice.id)
                    break
            assert "Language not found!"

        # TTS: configuration
        self.engine = pyttsx3.init()
        set_voice(self.engine, "EN-US")
        self.engine.setProperty("rate", 160)

        # Speech recognition settings
        self.__queue = queue.Queue()
        
        device_info= sd.query_devices(None, "input")
        self.__samplerate = int(device_info["default_samplerate"])
        model = Model(lang="en-us")
        self.rec = KaldiRecognizer(model, self.__samplerate)
    
    def __callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.__queue.put(bytes(indata))
        
    def read(self) -> str:
        with sd.RawInputStream(samplerate=self.__samplerate, blocksize = 8000, device=None,
            dtype="int16", channels=1, callback=self.__callback):
            while True:
                data = self.__queue.get()
                if self.rec.AcceptWaveform(data):
                    result = self.rec.Result()
                    print("Accepted as: " + result)
                    return json.loads(result)["text"]

    def write(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()