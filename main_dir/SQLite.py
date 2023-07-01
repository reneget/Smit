import sqlite3
import csv
import pandas as pd


def create_DB():
    # Установка соединения с базой данных SQLite
    conn = sqlite3.connect('commands_database.db')

    # Создание курсора для выполнения операций с базой данных
    cursor = conn.cursor()

    # Создание таблицы
    create_table_query = '''
    CREATE TABLE commands_table (
        id INTEGER PRIMARY KEY,
        user_title TEXT,
        tech_title TEXT,
        link TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    '''
    cursor.execute(create_table_query)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


def chek_DB():
    # Установка соединения с базой данных SQLite
    conn = sqlite3.connect('commands_database.db')

    # Создание курсора для выполнения операций с базой данных
    cursor = conn.cursor()

    # Выполнение запроса SQL для выборки данных
    select_query = 'SELECT * FROM commands_table'
    cursor.execute(select_query)

    # Получение результатов и сохранение в CSV файл
    with open('mydata.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # Запись заголовков столбцов
        csv_writer.writerows(cursor)

    # Закрытие соединения
    conn.close()


def append_command_in_DB(user_title, tech_title, link):
    connection = sqlite3.connect('commands_database.db')

    # Создание DataFrame с новой строкой
    new_data = {
        'user_title': user_title,
        'tech_title': tech_title,
        'link': link
    }
    df = pd.DataFrame([new_data])

    # Запись DataFrame в базу данных SQLite
    df.to_sql('commands_table', connection, if_exists='append', index=False)

    # Закрытие соединения
    connection.close()


def edit_command_in_DB(id, user_title, tech_title, link):

    connection = sqlite3.connect('commands_database.db')
    query = f"SELECT * FROM commands_table"
    df = pd.read_sql_query(query, connection)
    row = id
    # Внесите изменения в DataFrame
    if user_title != None:
        df.at[row, 'user_title'] = user_title
    if tech_title != None:
        df.at[row, 'tech_title'] = tech_title
    if link != None:
        df.at[row, 'link'] = link

    # Запись измененных данных обратно в таблицу SQLite
    df.to_sql('commands_table', connection, if_exists='replace', index=False)
    connection.close()


append_command_in_DB('включи игры', 'запуск приложения', 'Steam')
chek_DB()