import csv
import pandas as pd
import os

csv_file = 'commands_data.csv'


def create_csv():
    # Создание нового CSV-файла с заголовками
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'user_title', 'tech_title', 'link', 'created_at'])


def append_command(user_title, tech_title, link):
    # Чтение существующего CSV-файла в DataFrame
    df = pd.read_csv(csv_file)

    # Генерация нового ID для команды
    if df.empty:
        new_id = 1
    else:
        new_id = df['id'].max() + 1

    # Создание новой строки с данными команды
    new_row = {
        'id': new_id,
        'user_title': user_title,
        'tech_title': tech_title,
        'link': link,
        'created_at': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')
    }

    # Создание нового DataFrame с одной строкой
    new_df = pd.DataFrame([new_row])

    # Объединение существующего DataFrame и нового DataFrame
    df = pd.concat([df, new_df], ignore_index=True)

    # Сохранение DataFrame в CSV-файл
    df.to_csv(csv_file, index=False)


def edit_command(id, user_title=None, tech_title=None, link=None):
    # Чтение существующего CSV-файла в DataFrame
    df = pd.read_csv(csv_file)

    # Поиск строки с соответствующим ID
    row_index = df.index[df['id'] == id]

    if len(row_index) > 0:
        # Обновление указанных столбцов новыми значениями
        if user_title is not None:
            df.at[row_index, 'user_title'] = user_title
        if tech_title is not None:
            df.at[row_index, 'tech_title'] = tech_title
        if link is not None:
            df.at[row_index, 'link'] = link

        # Сохранение DataFrame в CSV-файл
        df.to_csv(csv_file, index=False)


def delete_command(index):
    # Чтение существующего CSV-файла в DataFrame
    df = pd.read_csv(csv_file)

    # Удаление строки по индексу
    df = df.drop(index - 1)

    # Перезапись изменений в CSV файл
    df.to_csv(csv_file, index=False)


def check_user_title(text):
    # Чтение CSV-файла в DataFrame
    df = pd.read_csv(csv_file)

    # Проверка условия: есть ли совпадение в столбце 'user_title' с заданным текстом
    match_found = df['user_title'].str.contains(text, case=False).any()

    # Возврат результата проверки
    return match_found


if not os.path.exists('commands_data.csv'):
    # Файл не существует, выполняем определенную функцию
    create_csv()
