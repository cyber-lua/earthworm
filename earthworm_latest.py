import random
import time
import os
import math
import string
import sys
import datetime
import itertools
import hashlib

# Utility functions
def make_variable(var_type, var_data):
    """Create a variable of the given type and data."""
    return eval(f"{var_type}({repr(var_data)})")

def calculate_factorial(n):
    """Return the factorial of n."""
    return math.factorial(n)

def fibonacci_sequence(n):
    """Return the first n numbers in the Fibonacci sequence."""
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def current_date():
    """Return the current date."""
    return datetime.date.today()

def current_time():
    """Return the current system time."""
    return datetime.datetime.now().time()

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_string(length=8):
    """Generate a random string of the given length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def create_hash(data, algorithm='md5'):
    """Create a hash of the given data using the specified algorithm."""
    h = hashlib.new(algorithm)
    h.update(data.encode())
    return h.hexdigest()

def read_file(path):
    """Read and return the contents of a file at the specified path."""
    with open(path, "r") as file:
        return file.read()

def write_file(path, contents):
    """Write the given contents to a file at the specified path."""
    with open(path, "w") as file:
        file.write(contents)

def list_directory(directory="."):
    """List all files and directories in the specified directory."""
    return os.listdir(directory)

def make_directory(path):
    """Create a directory at the specified path."""
    os.makedirs(path, exist_ok=True)

def remove_directory(path):
    """Remove a directory at the specified path."""
    os.rmdir(path)

def remove_file(path):
    """Remove a file at the specified path."""
    os.remove(path)

def get_file_size(path):
    """Return the size of a file at the specified path."""
    return os.path.getsize(path)

def get_file_extension(filename):
    """Return the file extension of the given filename."""
    return os.path.splitext(filename)[1]

def read_lines_from_file(path):
    """Read lines from a file and return them as a list."""
    with open(path, "r") as file:
        return file.readlines()

def append_to_file(path, contents):
    """Append the given contents to a file at the specified path."""
    with open(path, "a") as file:
        file.write(contents)

def get_file_creation_time(path):
    """Return the creation time of a file at the specified path."""
    return datetime.datetime.fromtimestamp(os.path.getctime(path))

def get_file_modification_time(path):
    """Return the modification time of a file at the specified path."""
    return datetime.datetime.fromtimestamp(os.path.getmtime(path))

def get_file_access_time(path):
    """Return the last access time of a file at the specified path."""
    return datetime.datetime.fromtimestamp(os.path.getatime(path))

def generate_uuid():
    """Generate and return a new UUID."""
    import uuid
    return uuid.uuid4()

def reverse_string(s):
    """Return the reverse of the given string."""
    return s[::-1]

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    return s == s[::-1]

def get_current_working_directory():
    """Return the current working directory."""
    return os.getcwd()

def change_directory(path):
    """Change the current working directory to the specified path."""
    os.chdir(path)

def sleep_for(seconds):
    """Pause the script for the given number of seconds."""
    time.sleep(seconds)

def countdown(seconds):
    """Perform a countdown from the given number of seconds."""
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up!")

def roll_dice(sides=6):
    """Simulate rolling a dice with the given number of sides (default is 6)."""
    return random.randint(1, sides)

def toss_coin():
    """Simulate a coin toss."""
    return random.choice(["Heads", "Tails"])

def find_max_in_list(lst):
    """Return the maximum value in the given list."""
    return max(lst)

def find_min_in_list(lst):
    """Return the minimum value in the given list."""
    return min(lst)

def calculate_sum(lst):
    """Return the sum of the values in the given list."""
    return sum(lst)

def calculate_average(lst):
    """Return the average of the values in the given list."""
    return sum(lst) / len(lst)

def calculate_median(lst):
    """Return the median of the values in the given list."""
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_standard_deviation(lst):
    """Return the standard deviation of the values in the given list."""
    mean = calculate_average(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)

def factorial(n):
    """Return the factorial of n."""
    return math.factorial(n)

def fibonacci(n):
    """Return the first n numbers in the Fibonacci sequence."""
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def is_even(n):
    """Check if the given number is even."""
    return n % 2 == 0

def is_odd(n):
    """Check if the given number is odd."""
    return n % 2 != 0

def convert_to_uppercase(s):
    """Convert the given string to uppercase."""
    return s.upper()

def convert_to_lowercase(s):
    """Convert the given string to lowercase."""
    return s.lower()

def capitalize_string(s):
    """Capitalize the first letter of the given string."""
    return s.capitalize()

def count_occurrences(lst, value):
    """Count the number of occurrences of the value in the given list."""
    return lst.count(value)

def find_index(lst, value):
    """Find the index of the first occurrence of the value in the given list."""
    return lst.index(value)

def sort_list(lst):
    """Sort the given list in ascending order."""
    return sorted(lst)

def reverse_list(lst):
    """Reverse the given list."""
    return lst[::-1]

def join_strings(lst, separator=" "):
    """Join the strings in the given list with the specified separator."""
    return separator.join(lst)

def split_string(s, separator=" "):
    """Split the given string by the specified separator."""
    return s.split(separator)

def remove_whitespace(s):
    """Remove leading and trailing whitespace from the given string."""
    return s.strip()

def replace_substring(s, old, new):
    """Replace all occurrences of the old substring with the new substring in the given string."""
    return s.replace(old, new)

def format_string(template, *args, **kwargs):
    """Format the given template string with the specified arguments and keyword arguments."""
    return template.format(*args, **kwargs)

def get_length(obj):
    """Return the length of the given object (string, list, tuple, etc.)."""
    return len(obj)

def convert_to_int(s):
    """Convert the given string to an integer."""
    return int(s)

def convert_to_float(s):
    """Convert the given string to a float."""
    return float(s)

def convert_to_str(obj):
    """Convert the given object to a string."""
    return str(obj)

def convert_to_list(s):
    """Convert the given string to a list of characters."""
    return list(s)

def get_absolute_value(n):
    """Return the absolute value of the given number."""
    return abs(n)

def round_number(n, decimals=0):
    """Round the given number to the specified number of decimal places."""
    return round(n, decimals)

def calculate_power(base, exponent):
    """Return the base raised to the power of the exponent."""
    return math.pow(base, exponent)

def calculate_square_root(n):
    """Return the square root of the given number."""
    return math.sqrt(n)

def calculate_logarithm(n, base=10):
    """Return the logarithm of the given number with the specified base."""
    return math.log(n, base)

def generate_random_float(min_val=0.0, max_val=1.0):
    """Generate a random float between min_val and max_val."""
    return random.uniform(min_val, max_val)

def shuffle_list(lst):
    """Shuffle the elements of the given list."""
    random.shuffle(lst)
    return lst

def sample_list(lst, k):
    """Return a sample of k elements from the given list."""
    return random.sample(lst, k)

def create_tuple(*args):
    """Create a tuple with the given arguments."""
    return tuple(args)

def create_set(*args):
    """Create a set with the given arguments."""
    return set(args)

def create_dict(**kwargs):
    """Create a dictionary with the given keyword arguments."""
    return dict(**kwargs)

def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries into one."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged

def filter_list(lst, condition):
    """Filter the given list based on the specified condition."""
    return [item for item in lst if condition(item)]

def map_list(lst, func):
    """Apply the given function to each element in the list."""
    return list(map(func, lst))

def reduce_list(lst, func, initializer=None):
    """Apply the given function cumulatively to the items in the list."""
    from functools import reduce
    return reduce(func, lst, initializer)

def flatten_list(nested_list):
    """Flatten a nested list."""
    return list(itertools.chain.from_iterable(nested_list))

def generate_combinations(lst, r):
    """Generate all r-length combinations of the elements in the list."""
    return list(itertools.combinations(lst, r))

def generate_permutations(lst, r=None):
    """Generate all r-length permutations of the elements in the list."""
    return list(itertools.permutations(lst, r))

def zip_lists(*lists):
    """Zip the given lists together."""
    return list(zip(*lists))

def enumerate_list(lst, start=0):
    """Enumerate the elements of the list, starting from the specified index."""
    return list(enumerate(lst, start))

def create_range(start, stop, step=1):
    """Create a range of numbers from start to stop with the specified step."""
    return list(range(start, stop, step))

def transpose_matrix(matrix):
    """Transpose the given matrix (list of lists)."""
    return list(map(list, zip(*matrix)))

def calculate_gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    return math.gcd(a, b)

def calculate_lcm(a, b):
    """Calculate the least common multiple of two numbers."""
    return abs(a * b) // math.gcd(a, b)

def check_subset(set1, set2):
    """Check if set1 is a subset of set2."""
    return set1.issubset(set2)

def check_superset(set1, set2):
    """Check if set1 is a superset of set2."""
    return set1.issuperset(set2)

def calculate_set_union(set1, set2):
    """Calculate the union of two sets."""
    return set1.union(set2)

def calculate_set_intersection(set1, set2):
    """Calculate the intersection of two sets."""
    return set1.intersection(set2)

def calculate_set_difference(set1, set2):
    """Calculate the difference between two sets."""
    return set1.difference(set2)

def calculate_set_symmetric_difference(set1, set2):
    """Calculate the symmetric difference between two sets."""
    return set1.symmetric_difference(set2)

def get_set_length(s):
    """Return the number of elements in the set."""
    return len(s)

def add_to_set(s, element):
    """Add an element to the set."""
    s.add(element)
    return s

def remove_from_set(s, element):
    """Remove an element from the set."""
    s.remove(element)
    return s

def pop_from_set(s):
    """Remove and return an arbitrary element from the set."""
    return s.pop()

def clear_set(s):
    """Remove all elements from the set."""
    s.clear()
    return s

def combine_sets(set1, set2):
    """Combine two sets using the union operator."""
    return set1 | set2

def intersect_sets(set1, set2):
    """Find the intersection of two sets."""
    return set1 & set2

def subtract_sets(set1, set2):
    """Subtract set2 from set1."""
    return set1 - set2

def symmetric_difference_sets(set1, set2):
    """Find the symmetric difference of two sets."""
    return set1 ^ set2

def create_frozenset(iterable):
    """Create a frozenset from the given iterable."""
    return frozenset(iterable)

def make_frozenset_union(set1, set2):
    """Combine two frozensets using the union operator."""
    return set1.union(set2)

def make_frozenset_intersection(set1, set2):
    """Find the intersection of two frozensets."""
    return set1.intersection(set2)

def make_frozenset_difference(set1, set2):
    """Find the difference of two frozensets."""
    return set1.difference(set2)

def make_frozenset_symmetric_difference(set1, set2):
    """Find the symmetric difference of two frozensets."""
    return set1.symmetric_difference(set2)

def check_frozenset_subset(set1, set2):
    """Check if set1 is a subset of set2."""
    return set1.issubset(set2)

def check_frozenset_superset(set1, set2):
    """Check if set1 is a superset of set2."""
    return set1.issuperset(set2)

def create_frozenset_copy(fset):
    """Create a shallow copy of a frozenset."""
    return frozenset(fset)

def check_if_empty(iterable):
    """Check if the given iterable is empty."""
    return not bool(len(iterable))

def reverse_iterable(iterable):
    """Return a reversed version of the given iterable."""
    return iterable[::-1]

def generate_arithmetic_sequence(start, stop, step=1):
    """Generate an arithmetic sequence from start to stop with the given step."""
    return list(range(start, stop, step))

def generate_geometric_sequence(start, ratio, n):
    """Generate a geometric sequence starting from start with the given ratio for n terms."""
    return [start * (ratio ** i) for i in range(n)]

def find_unique_elements(lst):
    """Find and return the unique elements in the given list."""
    return list(set(lst))

def flatten_deep_list(nested_list):
    """Flatten a deeply nested list."""
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten_deep_list(element))
        else:
            result.append(element)
    return result

def generate_primes(limit):
    """Generate all prime numbers up to the given limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def calculate_area_of_circle(radius):
    """Calculate the area of a circle with the given radius."""
    return math.pi * (radius ** 2)

def calculate_circumference_of_circle(radius):
    """Calculate the circumference of a circle with the given radius."""
    return 2 * math.pi * radius

def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle with the given length and width."""
    return length * width

def calculate_perimeter_of_rectangle(length, width):
    """Calculate the perimeter of a rectangle with the given length and width."""
    return 2 * (length + width)

def calculate_area_of_triangle(base, height):
    """Calculate the area of a triangle with the given base and height."""
    return 0.5 * base * height

def calculate_hypotenuse(a, b):
    """Calculate the hypotenuse of a right-angled triangle given sides a and b."""
    return math.sqrt(a**2 + b**2)

def solve_quadratic_equation(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0 and return the roots."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def convert_inches_to_centimeters(inches):
    """Convert inches to centimeters."""
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    """Convert centimeters to inches."""
    return cm / 2.54

def convert_pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.453592

def convert_kilograms_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg / 0.453592

def find_hcf(a, b):
    """Find the highest common factor (HCF) of two numbers."""
    return math.gcd(a, b)

def find_lcm(a, b):
    """Find the least common multiple (LCM) of two numbers."""
    return abs(a * b) // math.gcd(a, b)

def calculate_percentage(part, whole):
    """Calculate the percentage of part out of the whole."""
    return (part / whole) * 100

def calculate_average_speed(distance, time):
    """Calculate the average speed given distance and time."""
    return distance / time

def calculate_simple_interest(principal, rate, time):
    """Calculate the simple interest given principal, rate, and time."""
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time, n=1):
    """Calculate the compound interest given principal, rate, time, and number of times interest is compounded per year."""
    return principal * (1 + rate / (n * 100)) ** (n * time)

def convert_string_to_binary(s):
    """Convert a string to its binary representation."""
    return ' '.join(format(ord(char), '08b') for char in s)

def convert_binary_to_string(b):
    """Convert a binary representation to its string form."""
    return ''.join(chr(int(b, 2)) for b in b.split(' '))

def get_environment_variable(var):
    """Return the value of the specified environment variable."""
    return os.getenv(var)

def set_environment_variable(var, value):
    """Set the value of the specified environment variable."""
    os.environ[var] = value

def list_environment_variables():
    """List all environment variables."""
    return dict(os.environ)

def get_system_information():
    """Return system information."""
    return {
        "platform": sys.platform,
        "version": sys.version,
        "executable": sys.executable,
        "path": sys.path
    }

def get_current_datetime():
    """Return the current date and time."""
    return datetime.datetime.now()

def get_day_of_week(date):
    """Return the day of the week for the given date."""
    return date.strftime("%A")

def get_days_difference(date1, date2):
    """Return the difference in days between two dates."""
    return (date2 - date1).days

def get_month_name(month_number):
    """Return the name of the month for the given month number."""
    return datetime.date(1900, month_number, 1).strftime("%B")

def get_days_in_month(year, month):
    """Return the number of days in the given month and year."""
    return (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days if month != 12 else 31

def is_leap_year(year):
    """Check if the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_current_timestamp():
    """Return the current timestamp."""
    return time.time()

def convert_timestamp_to_datetime(timestamp):
    """Convert a timestamp to a datetime object."""
    return datetime.datetime.fromtimestamp(timestamp)

def get_elapsed_time(start_time):
    """Return the elapsed time since start_time."""
    return time.time() - start_time

def create_timer():
    """Create a timer object."""
    return {"start": time.time()}

def stop_timer(timer):
    """Stop the timer and return the elapsed time."""
    return time.time() - timer["start"]

def get_python_version():
    """Return the Python version."""
    return sys.version

def exit_program():
    """Exit the program."""
    sys.exit()

def get_file_lines_count(path):
    """Return the number of lines in the file at the specified path."""
    with open(path, "r") as file:
        return sum(1 for line in file)

def get_file_word_count(path):
    """Return the number of words in the file at the specified path."""
    with open(path, "r") as file:
        return sum(len(line.split()) for line in file)

def get_file_character_count(path):
    """Return the number of characters in the file at the specified path."""
    with open(path, "r") as file:
        return sum(len(line) for line in file)

def compare_files(file1, file2):
    """Compare two files and return True if they are identical, else False."""
    with open(file1, "r") as f1, open(file2, "r") as f2:
        return f1.read() == f2.read()

def copy_file(source, destination):
    """Copy a file from source to destination."""
    import shutil
    shutil.copyfile(source, destination)

def move_file(source, destination):
    """Move a file from source to destination."""
    import shutil
    shutil.move(source, destination)

def get_directory_size(directory):
    """Return the total size of all files in the specified directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def convert_string_to_hex(s):
    """Convert a string to its hexadecimal representation."""
    return s.encode("utf-8").hex()

def convert_hex_to_string(h):
    """Convert a hexadecimal representation to its string form."""
    return bytes.fromhex(h).decode("utf-8")

def get_local_ip_address():
    """Return the local IP address of the machine."""
    import socket
    return socket.gethostbyname(socket.gethostname())

def get_public_ip_address():
    """Return the public IP address of the machine."""
    import requests
    return requests.get("https://api.ipify.org").text

def create_zip_file(files, zip_name):
    """Create a zip file with the specified files."""
    import zipfile
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
    return zip_name

def extract_zip_file(zip_name, extract_to):
    """Extract the specified zip file to the specified directory."""
    import zipfile
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)
    return extract_to

def compress_string(s):
    """Compress the given string using zlib."""
    import zlib
    return zlib.compress(s.encode())

def decompress_string(c):
    """Decompress the given string using zlib."""
    import zlib
    return zlib.decompress(c).decode()

def generate_barcode(data):
    """Generate a barcode from the given data."""
    from barcode import Code128
    from barcode.writer import ImageWriter
    barcode = Code128(data, writer=ImageWriter())
    barcode.save('barcode')
    return 'barcode.png'

def generate_qr_code(data):
    """Generate a QR code from the given data."""
    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    return 'qrcode.png'
