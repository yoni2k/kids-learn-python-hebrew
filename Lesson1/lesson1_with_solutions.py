def return_str(str):
    """  תחזירו את המחרוזת שקיבלתם """
    return str


def string_twice(my_str):
    """  תחזירו את המחרוזת שקיבלתם פעמיים """
    return my_str*2


def string_twice_with_space(my_str):
    """ החזירו את המחרוזת פעמיים עם רווח באמצע """
    return my_str + ' ' + my_str


def string_twice_with_newline(my_str):
    """ החזירו את המחרוזת פעמיים עם שורה חדשה באמצע """
    return my_str + '\n' + my_str


def my_name_is(name):
    """
    מקבלים שם
    תחזירו בדיוק (כולל הגרשיים)
    My name is "<name>"
     """
    return "My name is \"" + name + "\""


def mult(a, b):
    """ החזירו כפל מספרים """
    return a * b


def mult_minus_sum(a, b):
    """
    החזירו הפרש בין כפל ובין סכום של מספרים
    דוגמא 1:
    a = 10
    b = 20
    כפל: 200
    סכום: 30
    הפרש:
        200 - 30 = 170
    """
    return (a * b) - (a + b)


def a_plus_b_mult_b_plus_c(a, b, c):
    """
        החזירו כפל של סכומים של a ו-b, וסכום של b ו-c
        דוגמא:
        a = 10
        b = 20
        c = 30
        סכום a ו-b:
            30
        סכום b ו-c:
            50
        כפל: 150
    """
    return (a + b) * (b + c)


"""
====================================================================================
    הזהרה: טסטים מפה והלאה - לא לרדת למטה
====================================================================================
    WARNING: TESTs from here, don't go down
====================================================================================    
"""


def test_return_str():
    my_str = "I love Python"
    ret = return_str(my_str)
    print(ret)
    assert ret == my_str


def test_string_twice():
    my_str = "AviadIdo"
    ret = string_twice(my_str)
    print(ret)
    assert (my_str*2) == ret


def test_string_twice_with_space():
    my_str = "AviadIdo"
    ret = string_twice_with_space(my_str)
    print(ret)
    assert (my_str + " " + my_str) == ret


def test_string_twice_with_newline():
    my_str = "AviadIdo"
    ret = string_twice_with_newline(my_str)
    print(ret)
    assert (my_str + "\n" + my_str) == ret


def test_my_name_is():
    name = "AviadIdo"
    ret = my_name_is(name)
    print(ret)
    assert ret == ("My name is \"" + name + "\"")


def test_mult():
    a = 3
    b = 4
    ret = mult(a, b)
    print(ret)
    assert ret == (a*b)
    assert mult(2, 5) == 10


def test_complex_math_statement1():
    a = 3
    b = 4
    ret = mult_minus_sum(a, b)
    print(ret)
    assert ret == (a * b) - (a + b)


def test_complex_math_statement2():
    a = 3
    b = 4
    c = 5
    ret = a_plus_b_mult_b_plus_c(a, b, c)
    print(ret)
    assert ret == (a + b) * (b + c)