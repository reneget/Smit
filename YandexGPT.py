import json
import requests
from yandexgptlite import YandexGPTLite

api_key = 'y0_AgAAAABlZTHJAATuwQAAAAEAyOnrAAAGiwlX4W9MVI90aYBU6dasy7PD_g'
account = YandexGPTLite('b1gmr6e38r1cull39olo', api_key)

def yandex_gpt(x):
    text = account.create_completion(
        str(x),
        '0.6',
        system_prompt='отвечай кратко, тебя зовут Смит'
    )
    print(text)
    return text

