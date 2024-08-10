# { Python: Быстрый старт, Тема: Базы данных }

import sqlite3


def get_connection():
    con = sqlite3.connect("notebook.sqlite3")
    con.execute("""
        CREATE TABLE IF NOT EXISTS data
        (name TEXT, phone TEXT, age INTEGER)
    """)
    return con


def insert_data(connection, name, phone, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)", (name, phone, age))
    connection.commit()
    print("Данные успешно добавлены")


def show_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    for el in cursor.fetchall():
        print(*el)


def update_data(connection, name, phone, age):
    cursor = connection.cursor()
    cursor.execute("UPDATE data SET name =?, phone =?, age =? WHERE name =?", (name, phone, age, name))
    connection.commit()
    print("Данные успешно обновлены")



def delete_by_name(connection, name):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE name = ?", (name,))
    connection.commit()
    print("Данные успешно удалены")


if __name__ == "__main__":
    print("Добро пожаловать в записную книжку!")

    action = None

    while action != 'exit':
        con = get_connection()
        action = input("Выберите действие [add, read, delete, update]\n")

        if action == 'add':
            try:
                name, phone, age = input("Введите данные (name phone age): ").split(" ")
            except ValueError:
                print("Неверно введены данные")
            else:
                insert_data(con, name, phone, age)
        elif action == 'read':
            show_data(con)
        elif action == 'delete':
            name_to_delete = input("Введите имя контакта на удаление: ")
            delete_by_name(con, name_to_delete)
        elif action == 'update':
            try:
                name, phone, age = input("Введите данные (name phone age): ").split(" ")
            except ValueError:
                print("Неверно введены данные")
            else:
                update_data(con, name, phone, age)


        else:
            con.close()
            print("Пока, пока")
            exit(0)
