from tts import tts_func
from stt import stt_funk
from commands import *
from CSV import *
from GUI import *

while True:
    text = stt_funk()
    if 'смит' in text and status_exit:
        tts_func('Слушаю вас')
        command_text = stt_funk()
        df = pd.read_csv('commands_data.csv')
        df = df[df['user_title'] == command_text]
        if df.empty:
            tts_func(f'Вы сказали, {command_text}, но в моём списке команд такой нет.')
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

            elif value == 'создай папку':
                tts_func(folder())
