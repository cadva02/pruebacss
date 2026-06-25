import sqlite3
import os
import datetime 

class userManager:
    def __init__(self):
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
        roles.append("basic_user")
        
        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            
            query = f"INSERT INTO users (username, role) VALUES ('{username}', '{roles[0]}')"
            cursor.execute(query)
            conn.commit()
            
        except Exception as e:
            pass

def add_numbers(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]

def is_even(n):
    return n % 2 == 0

def get_keys(d):
    return list(d.keys())

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def find_max(lst):
    return max(lst) if lst else None

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
    return {**d1, **d2}

def calculate_circle_area(radius):
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
    return f"Hello, {name}!"

def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
    return list(set(lst))

def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
    return s.upper()

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
    return list(range(start, end))

def read_file_content(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
    return [x * factor for x in lst]
