from tts import tts_func
from stt import stt_funk
from commands import *
from time import sleep as wait
import pandas as pd
import sqlite3
from SQLite import connection

while True:
    text = stt_funk()
    if 'скай' in text:
        tts_func('Слушаю вас')
        command_text = stt_funk()
        query = f"SELECT * FROM commands_table WHERE user_title = '{command_text}'"
        df = pd.read_sql_query(query, connection)
        if df.empty:
            tts_func(f'Вы сказали, {command_text}, но в моём списке комманд такой нет. Внесите её сами или не вносите, мне всё равно')
        else:
            value = df.iloc[0, 2]
            if value == 'открыть':
                open_link(df.iloc[0, 3])
                tts_func('Открываю вашу ссылку')

            elif value == 'узнать дату':
                tts_func(date_now())

            elif value == 'узнать время':
                tts_func(time_now())

            elif value == 'перезагрузка':
                tts_func(restart_system())

            elif value == 'отмена перезагрузки или выключения':
                tts_func(restart_cancellation())

            elif value == 'выключение устройства':
                tts_func(shutdown())

            elif value == 'запуск приложения':
                tts_func(start_app(df.iloc[0, 3]))

