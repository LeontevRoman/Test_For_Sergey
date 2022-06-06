import pytest
import sqlite3
from datetime import date


@pytest.fixture(scope='session')
def conn(request):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS client(id integer PRIMARY KEY autoincrement, name TEXT, change_date TEXT);")

    more_users = [('roman', date.today()), ('sergey', date.today()), ('nina', date.today()), ('dima', date.today())]
    cur.executemany("INSERT INTO client(name, change_date) VALUES(?, ?);", more_users)

    conn.commit()
    cur.execute("SELECT * FROM client")
    return conn

