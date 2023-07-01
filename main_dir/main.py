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
            value = df.iloc[0, 2]
            if value == 'открой':
                open_link(df.iloc[0, 3])
                stt_funk('Открываю вашу ссылку')

            elif value == 'узнать дату':
                stt_funk(date_now())

            elif value == 'узнать время':
                stt_funk(time_now())

            elif value == 'перезагрузка':
                stt_funk(restart_system())

            elif value == 'отмена перезагрузки или выключения':
                stt_funk(restart_cancellation())

            elif value == 'выключение устройства':
                stt_funk(shutdown())

            elif value == 'запуск приложения':
                stt_funk(start_app())

