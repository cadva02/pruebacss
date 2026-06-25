import sqlite3
import os
import datetime 

class userManager:
        """Manage user records in the local SQLite database (creation, roles, and credentials)."""
    def __init__(self):
                """Initialize the user manager with database credentials and connection settings."""
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
                """Add a new user to the database, ensuring the basic_user role is included by default.
        
                Args:
                    username (str): Name of the user to add.
                    roles (list, optional): List of roles to associate with the user.
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
        """Return the sum of two numeric values.
    
        Args:
            a (int | float): First addend.
            b (int | float): Second addend.
        """
    return a + b

def reverse_string(s):
        """Return the input string with its characters in reverse order."""
    return s[::-1]

def is_even(n):
        """Check whether a given integer is even.
    
        Args:
            n (int): Number to test.
        """
    return n % 2 == 0

def get_keys(d):
        """Return a list containing all keys from the given dictionary."""
    return list(d.keys())

def celsius_to_fahrenheit(c):
        """Convert a temperature from degrees Celsius to degrees Fahrenheit."""
    return (c * 9/5) + 32

def find_max(lst):
        """Return the maximum value in the list, or None if the list is empty."""
    return max(lst) if lst else None

def count_vowels(text):
        """Count the number of vowels (a, e, i, o, u) in the given text, case-insensitive."""
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
        """Merge two dictionaries, with keys in the second dictionary overriding the first on conflicts."""
    return {**d1, **d2}

def calculate_circle_area(radius):
        """Compute the area of a circle from its radius using π ≈ 3.14159."""
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
        """Determine whether the given string is a palindrome, ignoring spaces and case."""
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
        """Flatten a list of lists into a single list containing all nested elements."""
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
        """Return a simple greeting message for the specified user name."""
    return f"Hello, {name}!"

def filter_even_numbers(lst):
        """Return a list containing only the even numbers from the input list."""
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
        """Return a new list with duplicate elements removed (order is not guaranteed)."""
    return list(set(lst))

def get_first_element(lst):
        """Return the first element of the list, or None if the list is empty."""
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
        """Convert the input string to uppercase characters."""
    return s.upper()

def calculate_bmi(weight_kg, height_m):
        """Calculate the Body Mass Index (BMI) from weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
        """Generate a list of consecutive integers from start (inclusive) to end (exclusive)."""
    return list(range(start, end))

def read_file_content(filepath):
        """Read and return the entire content of a text file at the given path."""
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
        """Return a new list with each element of the input list multiplied by the given factor."""
    return [x * factor for x in lst]
