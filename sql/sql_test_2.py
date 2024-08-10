import sqlite3

# Создаем соединение с базой данных
con = sqlite3.connect('database.sqlite3')

# Выполняем операции с базой данных
with con:
    con.execute('INSERT INTO notebook VALUES ("Maria", "8(932)-222-11-12", 32)')
    con.execute("UPDATE notebook SET phone = '+7(932)-222-11-12' WHERE name = 'Maria'")
    con.execute("DELETE FROM notebook WHERE name = 'Maria'")
    # con.execute("DROP TABLE notebook")  # удаление таблицы

# Закрываем соединение явно
con.close()

# Проверяем, что соединение закрыто
try:
    con.execute('SELECT * FROM notebook')
    print("Соединение все еще открыто.")
except sqlite3.ProgrammingError:
    print("Соединение закрыто.")
