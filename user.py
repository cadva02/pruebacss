import sqlite3
import os
import datetime 

class userManager:
        """Manage user-related operations and interactions with the users database."""
    def __init__(self):
                """Initialize the user manager with default database credentials."""
        # SonarQube Vulnerability: Contraseña hardcodeada en el código.
        self.db_password = "super_secret_admin_pass!"
        self.db_user = "admin"

    def add_user(self, username, roles=[]):
                """Add a new user with the given username and roles to the database.
        
                Args:
                    username (str): Name of the user to add.
                    roles (list, optional): List of roles; "basic_user" is added by default.
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
        """Return the sum of two numbers.
    
        Args:
            a (int | float): First addend.
            b (int | float): Second addend.
        """
    return a + b

def reverse_string(s):
        """Return the given string reversed.
    
        Args:
            s (str): String to reverse.
        """
    return s[::-1]

def is_even(n):
        """Check whether a number is even.
    
        Args:
            n (int): Number to check.
        """
    return n % 2 == 0

def get_keys(d):
        """Return a list of keys from the given dictionary.
    
        Args:
            d (dict): Dictionary from which to extract keys.
        """
    return list(d.keys())

def celsius_to_fahrenheit(c):
        """Convert a temperature from Celsius to Fahrenheit.
    
        Args:
            c (float): Temperature in degrees Celsius.
        """
    return (c * 9/5) + 32

def find_max(lst):
        """Return the maximum value in a list or None if the list is empty.
    
        Args:
            lst (list): List of comparable elements.
        """
    return max(lst) if lst else None

def count_vowels(text):
        """Count the number of vowels in the given text (case-insensitive).
    
        Args:
            text (str): Text to analyze.
        """
    return sum(1 for char in text.lower() if char in 'aeiou')

def merge_dicts(d1, d2):
        """Merge two dictionaries, with keys from the second overriding the first.
    
        Args:
            d1 (dict): Base dictionary.
            d2 (dict): Dictionary whose values override d1 on key collisions.
        """
    return {**d1, **d2}

def calculate_circle_area(radius):
        """Calculate the area of a circle for a given radius.
    
        Args:
            radius (float): Radius of the circle.
        """
    return 3.14159 * (radius ** 2)

def is_palindrome(s):
        """Check if a string is a palindrome, ignoring spaces and case.
    
        Args:
            s (str): String to check.
        """
    clean_s = s.replace(" ", "").lower()
    return clean_s == clean_s[::-1]

def flatten_list(nested_list):
        """Flatten a list of lists into a single list.
    
        Args:
            nested_list (list[list]): List containing sublists to flatten.
        """
    return [item for sublist in nested_list for item in sublist]

def greet_user(name):
        """Return a greeting message for the given user name.
    
        Args:
            name (str): Name of the user to greet.
        """
    return f"Hello, {name}!"

def filter_even_numbers(lst):
        """Return a list containing only the even numbers from the input list.
    
        Args:
            lst (list[int]): List of integers to filter.
        """
    return [x for x in lst if x % 2 == 0]

def remove_duplicates(lst):
        """Return a new list with duplicate elements removed (order not guaranteed).
    
        Args:
            lst (list): List that may contain duplicate elements.
        """
    return list(set(lst))

def get_first_element(lst):
        """Return the first element of a list or None if the list is empty.
    
        Args:
            lst (list): List from which to get the first element.
        """
    if not lst:
        return None
    return lst[0]

def to_uppercase(s):
        """Convert the given string to uppercase.
    
        Args:
            s (str): String to convert.
        """
    return s.upper()

def calculate_bmi(weight_kg, height_m):
        """Calculate the Body Mass Index (BMI).
    
        Args:
            weight_kg (float): Weight in kilograms.
            height_m (float): Height in meters.
        """
    return weight_kg / (height_m ** 2)

def generate_range(start, end):
        """Generate a list of integers from start (inclusive) to end (exclusive).
    
        Args:
            start (int): Starting value of the range.
            end (int): Ending value (non-inclusive) of the range.
        """
    return list(range(start, end))

def read_file_content(filepath):
        """Read and return the entire content of a text file.
    
        Args:
            filepath (str): Path to the file to read.
        """
    with open(filepath, 'r') as file:
        return file.read()

def multiply_list(lst, factor):
        """Multiply each element of a list by the given factor.
    
        Args:
            lst (list[int | float]): List of numeric values.
            factor (int | float): Multiplier applied to each element.
        """
    return [x * factor for x in lst]
