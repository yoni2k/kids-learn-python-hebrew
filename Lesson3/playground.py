boolean = True
integer = 1
string = "Tomorrow morning will be hot"

print(type(True))  # stages: 1. type 2. print
print(type(1))
print(type("1"))

print(boolean)  # 1. get value of boolean = True 2. print

print(type(boolean))  # stages: 1. get value of boolean = True 2. type 3. print
print(type(integer))
print(type(string))

boolean = 1
integer = "My name is Yoni"
string = False

print()
print(type(boolean))
print(type(integer))
print(type(string))

print()
print(type(print))


def myfunc():
    pass


print(type(myfunc()))
print(type(myfunc))

print(type(2.0))

print(type(True))
print(type(True or False))
print(True or 1)
print(type(True or 1))
print(type(type))
print(type(type(True)))

age = 10
sentence = "My age is "

print(10 + 10)
print("10" + "10")

print(sentence + str(age))
print(10 + int("10"))
print(bool("True") and False)

