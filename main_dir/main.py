from tts import tts_func
from stt import stt_funk
from commands import *
from time import sleep as wait
import pandas as pd

while True:
    text = stt_funk()
    if 'скай' in text:
        tts_func('Слушаю вас')
        command_text = stt_funk()
        connection = sqlite3.connect('commands_database.db')
        query = f"SELECT * FROM commands_table WHERE user_title = '{command_text}'"
        df = pd.read_sql_query(query, connection)
        connection.close()
        if df.empty:
            tts_func(f'Вы сказали, {command_text}, но в моём списке комманд такой нет. Внесите её сами или идите нах')
        else:
            pass
