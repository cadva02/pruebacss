import sqlite3
import datetime


class UserManager:
    def __init__(self, db_user: str = "admin", db_password: str | None = None):
        """
        Initialize the user manager.

        db_password is provided externally to avoid hard-coded credentials in code.
        """
        self.db_password = db_password
        self.db_user = db_user

    def add_user(self, username, roles=None):
        if roles is None:
            roles = []

        roles.append("basic_user")

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            query = "INSERT INTO users (username, role) VALUES (?, ?)"
            cursor.execute(query, (username, roles[0]))
            conn.commit()
        except sqlite3.Error as db_error:
            # Log or re-raise the database-specific error to avoid swallowing exceptions silently
            raise RuntimeError(f"Database error occurred: {db_error}") from db_error
        finally:
            if "conn" in locals():
                conn.close()