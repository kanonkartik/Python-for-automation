def identify_type(variable):
    print(f"The data type of {variable} is {type(variable)}")

def int_to_float(x):
    return float(x)

def float_to_int(num):
    return int(num)

def str_to_int(y):
    return int(y)

def int_to_str(z):
    return str(z)

def concatenate_string(str1, str2):
    return str1 + str2

def add_numbers(a, b):
    return a + b

def update_dict(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def add_to_set(set_obj, element):
    set_obj.add(element)
    return set_obj

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Identify Data Types
identify_type(5)
identify_type(3.14)
identify_type("Hello")
identify_type([1, 2, 3])
identify_type({'name': 'John', 'age': 30})
identify_type({1, 2, 3})
identify_type(True)
identify_type(b'Hello')
identify_type(None)

# Convert Data Types
print(int_to_float(5))
print(float_to_int(3.14))
print(str_to_int("10"))
print(int_to_str(20))

# Manipulate Data Types
print(concatenate_string("Hello, ", "World!"))
print(add_numbers(10, 20))
print(update_dict({'name': 'John', 'age': 30}, 'age', 31))
print(add_to_set({1, 2, 3}, 4))

# Create and Use Custom Data Type
person = Person("Alice", 25)
print(person)