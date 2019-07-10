

"""
Python .py file
How to define a function
How to call a function
Why are functions necessary
Whitespace
Parameters to functions, multiple parameters to functions
Order of definitions of function and function call
Return from function

String "", '', or 3
string + operator
Escape character
Newline

"""

"""
def print_aviad(num_hello_world, num_hello_aviad):
    for i in range(num_hello_world):
        print("Hello World!")

    for i in range(num_hello_aviad):
        print("Hello Aviadi!")

    return "Done"


print(print_aviad(2, 3))
"""

""" 
def get_age_in_words(age):
    if age == 10:
        return "ten"
    if age == 12:
        return "twelve"


print(get_age_in_words(10))
print(get_age_in_words(12))
"""

"""
def print_my_age(age):
    print("Hello, nice to meet you, my age is: " + age)


print_my_age("ten")
print_my_age("five")
print_my_age("two")
"""

# print("Hello Aviad" + ", how are you?")

# My name is "Aviad"
"""
print("My name is \"Aviad\"")
print('My name is "Aviad"')
"""

"""
# AviadAviad
print("Hello\nmy\nname\nis\nAviad")
print("Aviad")
print("Aviad")
print("Hello\nmy\nname\nis\nAviad")
print("Hello\nmy\nname\nis\nAviad")
"""

"""
print(2 * 3 + 2 * 4 + 2 * 5 + 2 * 6 + 2 * 7 + 2 * 8)
print((2 * 3) + (2 * 4) + (2 * 5) + (2 * 6) + (2 * 7) + (2 * 8))
"""


def what_day_today():
    # return "Monday"
    return "Tuesday"


def test_what_day_today():
    assert what_day_today() == "Monday"


def return_with_space(my_str):
    """ Put code here """
    return my_str + " "


def test_return_with_space():
    print("Something")
    assert return_with_space("Aviad") == "Aviad "


print("Hi" + "\"" + "\'" + "\" " + "Avaid")
