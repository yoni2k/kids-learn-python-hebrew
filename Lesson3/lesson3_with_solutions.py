import pytest


def boolean_to_string(my_bool):
    """  תחזירו את הבוליאני שקיבלתם בתור מחזורת
    דוגמאות:
        True    ==> "True",
        False   ==> "False"
    """
    return str(my_bool)


def boolean_opposite_string(my_bool):
    """  תחזירו את ההפך מהבוליאני שקיבלתם בתור מחזורת
    דוגמאות:
        True    ==> "False",
        False   ==> "True"
    """
    return str(not my_bool)


def sum_ages(age1, age2):
    """  תחזירו את המשפט הבא עם סכום הגילאים שקיבלתם:
    דוגמאות:
        age1=10,    age2=12     ==> "Ages sum: 22",
        age1=0,     age2=5      ==> "Ages sum: 5",
    """
    return "Ages sum: " + str(age1 + age2)


def sum_ages_in_strings(str_age1, str_age2):
    """  תחזירו את סכום הגילאים שקיבלתם, הגילאים ניתנים כמחרוזות:
    דוגמאות:
        age1="10",    age2="12"     ==> 22,
        age1="0",     age2="5"      ==> 5,
    """
    return int(str_age1) + int(str_age2)


def boolean_string_opposite(str_bool):
    """  תחזירו את ההפך מהבוליאני בצורת מחרוזת שקיבלתם בתור בוליאני
    דוגמאות:
        "True"    ==> False,
        "False"   ==> True
    """
    return not eval(str_bool)


def get_type(var):
    """  תחזירו את סוג המשתנה שקיבלתם
    דוגמאות:
        2       ==> int,
        "Hi"    ==> str,
        "2"     ==> str,
        False   ==> bool
    """
    return type(var)


"""
====================================================================================
    הזהרה: טסטים מפה והלאה
====================================================================================
    WARNING: TESTs from here
====================================================================================    
"""


@pytest.mark.parametrize("my_bool, expected",
                         [
                             (True, "True"),
                             (False, "False")
                         ])
def test_boolean_to_string(my_bool, expected):
    ret = boolean_to_string(my_bool)
    print(f"Answer returned: \"{ret}\"")
    assert ret == expected


@pytest.mark.parametrize("my_bool, expected",
                         [
                             (True, "False"),
                             (False, "True")
                         ])
def test_boolean_opposite_string(my_bool, expected):
    ret = boolean_opposite_string(my_bool)
    print(f"Answer returned: \"{ret}\"")
    assert ret == expected


@pytest.mark.parametrize("age1, age2, expected",
                         [
                             (1,    2,  "Ages sum: 3"),
                             (10,   12, "Ages sum: 22"),
                         ])
def test_sum_ages(age1, age2, expected):
    ret = sum_ages(age1, age2)
    print(f"Answer returned: \"{ret}\"")
    assert ret == expected


@pytest.mark.parametrize("str_age1, str_age2, expected",
                         [
                             ("1",  "2",  3),
                             ("10", "12", 22),
                         ])
def test_sum_ages(str_age1, str_age2, expected):
    ret = sum_ages_in_strings(str_age1, str_age2)
    print(f"Answer returned: {ret}")
    assert ret == expected


@pytest.mark.parametrize("str_bool, expected",
                         [
                             ("True", False),
                             ("False", True)
                         ])
def test_boolean_string_opposite(str_bool, expected):
    ret = boolean_string_opposite(str_bool)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("var, expected",
                         [
                             (1, int),
                             ("1", str),
                             (True, bool),
                             (False, bool),
                             (1.1, float),
                             ((1, 2), tuple),
                             ([1, 2], list),
                             (range(1, 3), range),
                             ({1: "1"}, dict),
                             (set((1, 2)), set)
                         ])
def test_boolean_string_opposite(var, expected):
    ret = get_type(var)
    print("Answer returned: " + str(ret))
    assert ret == expected


