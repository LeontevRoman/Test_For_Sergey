import sqlite3
from datetime import date


def test_insert(conn):
    cur = conn.cursor()

    insert_list = list()
    insert_list.append('mariya')
    insert_list.append(str(date.today()))

    assert cur.execute("INSERT INTO client(name, change_date) VALUES(?, ?);", tuple(insert_list)), 'WTF???'
    print()
    cur.execute("SELECT * FROM client")
    print(cur.fetchall())
    print('Данные успешно добавлены')
    conn.commit()


def test_edit(conn):
    cur = conn.cursor()
    insert_list = ('nikolay', date.today())

    assert cur.execute("UPDATE client SET name = ?, change_date = ? WHERE id = '3';", insert_list), 'Сорян, Кривые данные'
    print()
    print('Данные успешно изменены')
    cur.execute("SELECT * FROM client")
    print(cur.fetchall())
    conn.commit()


def test_delete(conn):
    cur = conn.cursor()

    assert cur.execute("DELETE FROM client WHERE id = '4'"), 'Сорян, Таблица пуста'
    print()
    print('Данные успешно удалены')
    cur.execute("SELECT * FROM client")
    print(cur.fetchall())
    conn.commit()


