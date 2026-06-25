import sqlite3
import os
import datetime 

class userManager:
        """Manage user-related operations, including database-backed user creation and role assignment."""
    def __init__(self):
                """Initialize the user manager with database connection credentials."""
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
                """Add a new user to the database with the given username and roles, ensuring a basic role is present."""
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
        """Return a new string with the characters of s in reverse order."""
    return s[::-1]

def is_even(n):
        """Return True if the integer n is even, otherwise False."""
    return n % 2 == 0

def get_keys(d):
        """Return a list containing all keys from the dictionary d."""
    return list(d.keys())

def celsius_to_fahrenheit(c):
        """Convert a temperature in Celsius c to Fahrenheit and return the result."""
    return (c * 9/5) + 32

def find_max(lst):
        """Return the maximum value in lst, or None if the list is empty."""
    return max(lst) if lst else None

def count_vowels(text):
        """Count and return the number of vowel characters in the given text string."""
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
        """Return a new dictionary resulting from merging dictionaries d1 and d2, with d2 overriding duplicate keys."""
    return {**d1, **d2}

def calculate_circle_area(radius):
        """Compute and return the area of a circle given its radius using a fixed approximation of pi."""
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
        """Return True if s is a palindrome ignoring spaces and case, otherwise False."""
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
        """Flatten a list of lists into a single list containing all nested elements in order."""
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
        """Return a greeting string addressed to the user with the provided name."""
    return f"Hello, {name}!"

def filter_even_numbers(lst):
        """Return a list containing only the even integers from the input list lst."""
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
        """Return a new list containing the unique elements from lst, with order not guaranteed."""
    return list(set(lst))

def get_first_element(lst):
        """Return the first element of lst, or None if the list is empty or falsy."""
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
        """Return an uppercase version of the input string s."""
    return s.upper()

def calculate_bmi(weight_kg, height_m):
        """Calculate and return the Body Mass Index (BMI) given weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
        """Return a list of integers starting from start up to but not including end."""
    return list(range(start, end))

def read_file_content(filepath):
        """Read and return the entire text content of the file located at filepath."""
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
        """Return a new list where each element of lst is multiplied by the given factor."""
    return [x * factor for x in lst]
