import datetime
import os
import webbrowser as wb

import pendulum
from AppOpener import open


def open_link(link):
    wb.open_new_tab(link)


def date_now():
    pendulum.set_locale('ru')
    date = str(datetime.date.today()).split('-')
    print(date)
    dt = pendulum.datetime(int(date[0]), int(date[1]), int(date[2]))
    return dt.format('dddd, DD MMMM YYYY') + ' года'


def time_now():
    current_time = datetime.datetime.now()
    hours = current_time.hour
    minutes = current_time.minute
    return f"{hours} {minutes}"


def restart_system():  # перезагрузка компьютера через 30 сек
    os.system(" shutdown /r /t 30 ")
    return 'компьютер будет перезапущен через тридцать секунд'


def restart_cancellation():
    os.system(" shutdown /a ")
    return 'отмена выключения компьютера'


def shutdown():  # выключение компьютера через 5 сек
    os.system(" shutdown /s /t 30 ")
    return 'компьютер будет выключен через тридцать секунд'


def start_app(name):  # открыть приложение
    open(name)
    return f'открывается приложение {name}'


def folder():  # создать папку
    os.chdir(os.path.expanduser('~') + r'\Desktop')
    if not os.path.isdir("Новая папка"):
        os.mkdir("Новая папка")
