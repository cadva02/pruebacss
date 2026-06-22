import sqlite3
import os


class UserManager:
    def __init__(self):
        self.db_password = os.getenv("DB_PASSWORD", "super_secret_admin_pass!")
        self.db_user = os.getenv("DB_USER", "admin")

    def add_user(self, username, roles=None):
        if roles is None:
            roles = []
        roles.append("basic_user")
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            query = "INSERT INTO users (username, role) VALUES (?, ?)"
            cursor.execute(query, (username, roles[0]))
            conn.commit()
        except sqlite3.DatabaseError as ex:
            raise RuntimeError("Database error while adding user") from ex
        finally:
            if 'conn' in locals():
                conn.close()