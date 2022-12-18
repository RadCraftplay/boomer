from abc import ABC, abstractmethod
import io
import json
import speech_recognition as sr
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
    def read(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        
        model = Model("model")
        rec = KaldiRecognizer(model, audio.sample_rate)

        b_handle = io.BytesIO()
        b_handle.write(audio.get_wav_data())
        b_handle.seek(0)
        wf = io.BufferedReader(b_handle)
        
        while True:
            data = wf.read(2000)
            if len(data) == 0:
                break
        
        res = json.loads(rec.FinalResult())
        print(res)

        return res["text"]

    def write(self, text: str):
        print(text)