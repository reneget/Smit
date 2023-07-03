import sqlite3
import csv
import pandas as pd

connection = sqlite3.connect('commands_database.db')
def create_DB(connection):
    # Установка соединения с базой данных SQLite
    conn = connection

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


def chek_DB(connection):
    # Установка соединения с базой данных SQLite
    conn = connection

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


def append_command_in_DB(connection, user_title, tech_title, link):

    # Создание DataFrame с новой строкой
    new_data = {
        'user_title': user_title,
        'tech_title': tech_title,
        'link': link
    }
    df = pd.DataFrame([new_data])

    # Запись DataFrame в базу данных SQLite
    df.to_sql('commands_table', connection, if_exists='append', index=False)
    connection.commit()


def edit_command_in_DB(connection, id, user_title, tech_title, link):
    cursor = connection.cursor()
    if user_title != 'None':
        cursor.execute(f"UPDATE commands_table SET 'user_title' = '{user_title}' WHERE id = {id}")
    if tech_title != 'None':
        cursor.execute(f"UPDATE commands_table SET 'tech_title' = '{tech_title}' WHERE id = {id}")
    if link != 'None':
        cursor.execute(f"UPDATE commands_table SET 'link' = '{link}' WHERE id = {id}")
    connection.commit()


def delet_in_DB(connection, id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM commands_table WHERE id = {id}")
    connection.commit()

# create_DB(connection)
# delet_in_DB(connection, 9)
# edit_command_in_DB()
chek_DB(connection)
