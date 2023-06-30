from tts import tts_func
from stt import stt_funk
from commands import *
from time import sleep as wait

while True:
    text = stt_funk()
    if 'скай' in text:
        tts_func('Слушаю вас')