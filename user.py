import sqlite3
import os
import datetime 

class userManager:
        """Manage user-related operations backed by a SQLite database."""
    def __init__(self):
                """Initialize the user manager with database credentials."""
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
                """Add a new user with the given username and roles into the database."""
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
        """Return the sum of two numbers a and b."""
    return a + b

def reverse_string(s):
        """Return the reverse of the input string s."""
    return s[::-1]

def is_even(n):
        """Return True if n is an even integer, otherwise False."""
    return n % 2 == 0

def get_keys(d):
        """Return a list of keys from the given dictionary d."""
    return list(d.keys())

def celsius_to_fahrenheit(c):
        """Convert a temperature in Celsius c to Fahrenheit and return it."""
    return (c * 9/5) + 32

def find_max(lst):
        """Return the maximum value in lst, or None if the list is empty."""
    return max(lst) if lst else None

def count_vowels(text):
        """Count and return the number of vowels in the given text string."""
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
        """Return a new dictionary containing keys and values from d1 and d2, with d2 overwriting duplicates."""
    return {**d1, **d2}

def calculate_circle_area(radius):
        """Calculate and return the area of a circle with the given radius."""
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
        """Return True if s is a palindrome ignoring spaces and case, otherwise False."""
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
        """Flatten a list of lists into a single list and return it."""
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
        """Return a greeting string for the given user name."""
    return f"Hello, {name}!"

def filter_even_numbers(lst):
        """Return a list containing only the even numbers from lst."""
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
        """Return a new list with duplicate elements removed from lst."""
    return list(set(lst))

def get_first_element(lst):
        """Return the first element of lst, or None if the list is empty."""
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
        """Return the uppercase version of the input string s."""
    return s.upper()

def calculate_bmi(weight_kg, height_m):
        """Calculate and return the BMI given weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
        """Return a list of integers from start (inclusive) to end (exclusive)."""
    return list(range(start, end))

def read_file_content(filepath):
        """Read and return the entire text content of the file at the given filepath."""
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
        """Return a new list with each element of lst multiplied by the given factor."""
    return [x * factor for x in lst]
