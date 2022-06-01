import sqlite3 as sl
from enum import Enum


class UserState(Enum):
    OFFICE = 'office'
    REMOTE = 'remote'
    REST = 'rest'


class Database:
    def __init__(self, db_pass: str):
        self.connection = sl.connect(db_pass)

    def create_tables(self):
        self.connection.cursor().execute('''CREATE TABLE IF NOT EXISTS users (
                                         user_id INTEGER PRIMARY KEY,
                                         username TEXT,
                                         first_name TEXT,
                                         last_name TEXT,
                                         work_office BOOLEAN DEFAULT FALSE,
                                         work_remote BOOLEAN DEFAULT FALSE,
                                         rest BOOLEAN DEFAULT FALSE)''')

    def user_exists(self, user_id: int) -> bool:
        answer = self.connection.cursor().execute('SELECT user_id FROM users WHERE user_id = ?',
                                                  (user_id,)).fetchmany(1)
        return bool(len(answer))

    def add_user(self, user_id: int, username: str, first_name: str, last_name: str) -> None:
        self.connection.cursor().execute('''INSERT INTO users (user_id, username, first_name, last_name) 
                                             VALUES (?, ?, ?, ?)''', (user_id, username, first_name, last_name))
        self.connection.commit()

    def remove_user(self, user_id: int) -> None:
        self.connection.cursor().execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        self.connection.commit()

    def get_all_user_id(self) -> list:
        return self.connection.cursor().execute('SELECT user_id FROM users').fetchall()

    def set_state(self, user_id: int, state: UserState, value: bool):
        cur = self.connection.cursor()
        match state:
            case UserState.OFFICE:
                cur.execute('UPDATE users SET work_office = ? WHERE user_id = ?', (value, user_id))
                self.connection.commit()
            case UserState.REMOTE:
                cur.execute('UPDATE users SET work_remote = ? WHERE user_id = ?', (value, user_id))
                self.connection.commit()
            case UserState.REST:
                cur.execute('UPDATE users SET rest = ? WHERE user_id = ?', (value, user_id))
                self.connection.commit()

    def set_all_false(self):
        self.connection.cursor().execute('UPDATE users SET work_office = False, work_remote = False, rest = False')
        self.connection.commit()
