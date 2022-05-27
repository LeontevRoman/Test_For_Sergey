import pytest
import sqlite3


@pytest.fixture(scope='function')
def conn(request):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS client(
           id INT PRIMARY KEY,
           name TEXT,
           change_date TEXT);
        """)
    conn.commit()
    return conn

