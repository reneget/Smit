from CSV import *
from commands import *
from stt import stt_funk
# from tts import tts_func
from tts_AI import ai_tts as tts_func
from mp3_play import play_mp3
from YandexGPT import yandex_gpt

while True:
    text = stt_funk()
    if 'смит' in text:
        # tts_func('Слушаю вас.')
        play_mp3('Слушаю вас')
        command_text = stt_funk()
        df = pd.read_csv('commands_data.csv')
        df = df[df['user_title'] == command_text]
        if df.empty:
            # tts_func(f'Хм-м, Вы сказали, {command_text}, но в моём списке команды такой нет...')
            # play_mp3('команды нет')
            tts_func(yandex_gpt(command_text))

        else:
            value = df.iloc[0, 2]
            if value == 'открой' or value == 'рой' or value == 'ютуб':
                open_link(df.iloc[0, 3])
                play_mp3('Открываю вашу ссылку')

            elif value == 'привет' or value == 'пивет' or value == 'здравствуй':
                play_mp3('Здравствуйте')

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
