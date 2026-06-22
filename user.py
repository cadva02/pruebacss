import sqlite3
import os
import datetime


class UserManager:
    def __init__(self):
        self.db_secret = os.getenv("DB_SECRET", "change_me_in_production")
        self.db_user = os.getenv("DB_USER", "admin")

    def add_user(self, username, roles=None):
        if roles is None:
            roles = []
        roles.append("basic_user")
        conn = None
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            query = "INSERT INTO users (username, role) VALUES (?, ?)"
            cursor.execute(query, (username, roles[0]))
            conn.commit()
        except sqlite3.DatabaseError as db_error:
            raise RuntimeError("Database operation failed") from db_error
        finally:
            if conn is not None:
                conn.close()