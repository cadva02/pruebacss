import sqlite3
import os
# SonarQube Smell: Importación no utilizada (Unused import)
import datetime 

# SonarQube Smell: El nombre de la clase debería seguir PascalCase (UserManager), no camelCase.
class userManager:
    def __init__(self):
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    # SonarQube Bug Crítico: Argumento por defecto mutable (roles=[]). 
    # En Python, esa lista se comparte entre TODAS las llamadas a la función, causando bugs muy difíciles de rastrear.
    def add_user(self, username, roles=[]):
        roles.append("basic_user")
        
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            
            # SonarQube Vulnerability: Inyección SQL. Usar concatenación o f-strings directamente en consultas es muy peligroso.
            query = f"INSERT INTO users (username, role) VALUES ('{username}', '{roles[0]}')"
            cursor.execute(query)
            conn.commit()
            
        except Exception as e:
            # SonarQube Smell/Bug: Capturar la excepción base 'Exception' y no hacer nada (Swallowing exception). 
            # Esto silencia errores reales de la aplicación.
            pass
