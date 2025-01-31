import json

import pyaudio
from vosk import Model, KaldiRecognizer

model = Model("vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def stt_funk():
    def rec_speech():
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                message = json.loads(rec.Result())
                if message['text']:
                    yield message['text']

    for text in rec_speech():
        return text
