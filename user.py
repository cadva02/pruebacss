import sqlite3
import os
import datetime 

class userManager:
        """Manage user records in the local SQLite users database."""
    def __init__(self):
                """Initialize the user manager with database credentials."""
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
                """Add a new user with at least a basic_user role to the database.
        
                Args:
                    username: Name of the user to add.
                    roles: Optional list of roles; "basic_user" will always be appended.
                """
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
        """Return the sum of two numbers."""
    return a + b

def reverse_string(s):
        """Return the reversed version of the given string."""
    return s[::-1]

def is_even(n):
        """Return True if n is an even integer, otherwise False."""
    return n % 2 == 0

def get_keys(d):
        """Return a list of keys from the given dictionary."""
    return list(d.keys())

def celsius_to_fahrenheit(c):
        """Convert a temperature in Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def find_max(lst):
        """Return the maximum value in the list, or None if the list is empty."""
    return max(lst) if lst else None

def count_vowels(text):
        """Count and return the number of vowels in the given text string."""
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
        """Return a new dictionary containing the merged contents of d1 and d2."""
    return {**d1, **d2}

def calculate_circle_area(radius):
        """Calculate the area of a circle given its radius."""
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
        """Return True if the string is a palindrome, ignoring spaces and case."""
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
        """Flatten a list of lists into a single list of items."""
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
        """Return a greeting message addressed to the given user name."""
    return f"Hello, {name}!"

def filter_even_numbers(lst):
        """Return a list containing only the even numbers from the input list."""
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
        """Return a new list with duplicate elements removed (order not guaranteed)."""
    return list(set(lst))

def get_first_element(lst):
        """Return the first element of the list, or None if the list is empty."""
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
        """Return an uppercase version of the given string."""
    return s.upper()

def calculate_bmi(weight_kg, height_m):
        """Calculate and return the body mass index (BMI).
    
        Args:
            weight_kg: Weight in kilograms.
            height_m: Height in meters.
        """
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
        """Return a list of integers from start (inclusive) to end (exclusive)."""
    return list(range(start, end))

def read_file_content(filepath):
        """Read and return the full contents of a text file at the given path."""
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
        """Return a new list where each element is multiplied by the given factor."""
    return [x * factor for x in lst]
