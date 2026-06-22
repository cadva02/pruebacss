import sqlite3
import os
import datetime


class UserManager:
    def __init__(self):
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    # SonarQube Bug Crítico: Argumento por defecto mutable (roles=[]).
    # En Python, esa lista se comparte entre TODAS las llamadas a la función, causando bugs muy difíciles de rastrear.
    def add_user(self, username, roles=None):
        if roles is None:
            roles = []
        roles.append("basic_user")
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            # SonarQube Vulnerability: Inyección SQL.
            # Usar parámetros en lugar de concatenación o f-strings directamente en consultas.
            query = "INSERT INTO users (username, role) VALUES (?, ?)"
            cursor.execute(query, (username, roles[0]))
            conn.commit()
        except Exception:
            # SonarQube Smell/Bug: Capturar la excepción base 'Exception' y no hacer nada (Swallowing exception).
            # Esto silencia errores reales de la aplicación. CON REGLAS
            raise