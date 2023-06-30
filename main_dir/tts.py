from win32com.client import Dispatch as DS

def tts_func(text):
    speak = DS("SAPI.SpVoice").Speak
    speak(text)
    print(text)
