"""
print("Hello World!")

print(2 + 3)

print((1 + 2) * (3 + 4))

print(1 + 2 * 3 + 4)

print((2 * 3) + (2 * 4) + (2 * 5))
print(2 * 3 + 2 * 4 + 2 * 5)

print("Ido")
print('Ido')

# My name is "Ido"
print('My name is "Ido"')

print("My name is \"Ido\"")

print("My\nname\nis\nIdo")

# hi\bye
print("hi\\bye")

print("Hi" + "Ido" + "how" + "are" + "you")
print("Hi " + "Ido, " + "how " + "are " + "you?")

"""

"""
def my_first_function():
    print("This is my first function")
    print("I love Ido")
print("I love Ido very much")

my_first_function()
my_first_function()
"""

"""
def square_func(a):
    print(a*a)

square_func(2)
square_func(3)
square_func(2131)
"""

"""
def plus(a, b):
    print(a + b)

plus(2, 3)
plus(2, 8)
"""

def plus(a, b):
    return a + b

#print(plus(2, 3))

def test_plus():
    assert plus(2, 3) == 5
    assert plus(3, 4) == 7
