import sqlite3
import os
import datetime 

class userManager:
        """Manage user records and interactions with the underlying SQLite users database."""
    def __init__(self):
                """Initialize the user manager and configure default database credentials."""
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
                """Add a new user with a basic role to the users database.
        
                Args:
                    username (str): Name of the user to create.
                    roles (list, optional): List of roles, with 'basic_user' appended by default.
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
        """Return the sum of two numeric values a and b."""
    return a + b

def reverse_string(s):
        """Return the input string s reversed."""
    return s[::-1]

def is_even(n):
        """Determine whether the integer n is even.
    
        Returns True if n is even, otherwise False.
        """
    return n % 2 == 0

def get_keys(d):
        """Return a list of keys from the dictionary d."""
    return list(d.keys())

def celsius_to_fahrenheit(c):
        """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return (c * 9/5) + 32

def find_max(lst):
        """Return the maximum value in lst, or None if the list is empty."""
    return max(lst) if lst else None

def count_vowels(text):
        """Count the number of vowels (a, e, i, o, u) in the given text, case-insensitive."""
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
        """Merge two dictionaries, returning a new dict where keys from d2 override those in d1."""
    return {**d1, **d2}

def calculate_circle_area(radius):
        """Calculate the area of a circle for the given radius using π ≈ 3.14159."""
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
        """Check if the string s is a palindrome, ignoring spaces and case."""
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
        """Flatten a list of lists into a single list containing all the elements."""
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
        """Return a greeting message addressed to the given name."""
    return f"Hello, {name}!"

def filter_even_numbers(lst):
        """Return a list containing only the even numbers from the input list lst."""
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
        """Return a list with duplicate elements removed from lst (order not guaranteed)."""
    return list(set(lst))

def get_first_element(lst):
        """Return the first element of lst, or None if the list is empty."""
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
        """Convert the input string s to uppercase and return it."""
    return s.upper()

def calculate_bmi(weight_kg, height_m):
        """Calculate the Body Mass Index (BMI) from weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
        """Generate a list of integers from start up to but not including end."""
    return list(range(start, end))

def read_file_content(filepath):
        """Read and return the entire text content of the file at the given filepath."""
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
        """Return a new list where each element of lst is multiplied by the given factor."""
    return [x * factor for x in lst]
