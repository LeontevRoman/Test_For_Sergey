import sqlite3

choise = input('Введите что будем тестить (insert, edit, delete)? : ')


if choise == 'insert':
    def test_insert(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM client')

        leight_table = len(cur.fetchall())
        insert_list = list()
        insert_list.append(str(leight_table + 1))
        insert_list.append(input('Введите имя : '))
        insert_list.append(input('Введите дату в формате ****-**-** : '))
        print(tuple(insert_list))
        assert cur.execute("INSERT INTO client(id, name, change_date) VALUES(?, ?, ?);", tuple(insert_list)), 'WTF???'
        print('Данные успешно добавлены')
        conn.commit()

if choise == 'edit':
    def test_edit(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM client')
        insert_list = list()
        n = int(input('Введите номер записи: '))
        leight_table = cur.fetchall()

        insert_list.append(input('Введите новое имя : '))
        insert_list.append(input('Введите новую дату в формате ****-**-** : '))
        try:
            insert_list.append(leight_table[n-1][0])
        except IndexError:
            print('Нет такой записи')
        assert cur.execute("UPDATE client SET name = ?, change_date = ? WHERE id = ?", tuple(insert_list)), 'Сорян, Кривые данные'
        print('Данные изменены')
        conn.commit()

if choise == 'delete':
    def test_delete(conn):
        cur = conn.cursor()
        cur.execute('SELECT * FROM client')

        leight_table = len(cur.fetchall())
        delete_y_n = input('Удаляем последнюю записть, Вы уверены y/n')
        if delete_y_n == 'y':
            assert cur.execute("DELETE FROM client WHERE id = ?", (leight_table, )), 'Сорян, Таблица пуста'
            print('Последняя запись удалена')
            conn.commit()
        else:
            pass


