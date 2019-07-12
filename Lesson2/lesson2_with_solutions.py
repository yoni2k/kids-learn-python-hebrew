import pytest


def opposite(my_bool):
    """  תחזירו את ההפך ממה שקיבלתם
    דוגמאות:
        True    ==> False,
        False   ==> True
    """
    return not my_bool


def did_get_two(my_int):
    """  תחזירו True אם מהמספר שקיבלתם שווה 2, ו-False אחרת
    דוגמאות:
        2 ==> True,
        1 ==> False,
        3 ==> False
    """
    return my_int == 2


def did_not_get_two1(my_int):
    """  תחזירו True אם מהמספר שקיבלתם לא שווה 2, ו-False אחרת
    דוגמאות:
        2 ==> False,
        1 ==> True,
        3 ==> True
    """
    return my_int != 2


def did_not_get_two2(my_int):
    """  תחזירו True אם מהמספר שקיבלתם לא שווה 2, ו-False אחרת
    תעשו את זה בדרך שונה מהדרך בה השתמשתם ב-did_not_get_two1
    דוגמאות:
        2 ==> False,
        1 ==> True,
        3 ==> True
    """
    return not (my_int == 2)


def numbers_equal(my_int1, my_int2):
    """  תחזירו True אם המספרים שווים, ו-False אחרת
    דוגמאות:
        my_int1=1, my_int2=1 ==> True,
        my_int1=1, my_int2=2 ==> False,
        my_int1=2, my_int2=1 ==> False,
        my_int1=2, my_int2=2 ==> True,
    """
    return my_int1 == my_int2


def is_between_2_and_5(num):
    """  תחזירו True אם מהמספר הוא בין 2 ו-5 (לא כולל 2 ו-5), ו-False אחרת
    דוגמאות:
        num=1 ==> False,
        num=2 ==> False,
        num=3 ==> True,
        num=6 ==> False
    """
    return (num > 2) and (num < 5)


def is_between_numbers(num, a, b):
    """  תחזירו True אם מהמספר הוא בין a ו-b (לא כולל a ו-b), ו-False אחרת
    נתון ש-a קטן מ-b
    דוגמאות:
        num=1, a=2, b=5 ==> False,
        num=2, a=2, b=5 ==> False,
        num=3, a=2, b=5 ==> True,
        num=6, a=2, b=5 ==> False
    """
    return (num > a) and (num < b)


def not_in_elementary_school(age):
    """  קיבלתם גיל של בן אדם, תחזירו True אם הוא בטוח לא בגיל יסודי (עד 6 כולל, ו-13 ומעלה), ו-False אחרת
    דוגמאות:
        age=5   ==> True,
        age=6   ==> True,
        age=7   ==> False,
        age=8   ==> False,
        age=13  ==> True,
    """
    return (age <= 6) or (age >= 13)


"""
====================================================================================
    אזהרה: טסטים מפה והלאה
====================================================================================
    WARNING: TESTs from here
====================================================================================    
"""


@pytest.mark.parametrize("my_bool, expected",
                         [
                             (True, False),
                             (False, True)
                         ])
def test_opposite(my_bool, expected):
    ret = opposite(my_bool)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("my_int, expected",
                         [
                             (2, True),
                             (1, False),
                             (3, False)
                         ])
def test_did_get_two(my_int, expected):
    ret = did_get_two(my_int)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("my_int, expected",
                         [
                             (2, False),
                             (1, True),
                             (3, True)
                         ])
def test_did_not_get_two1(my_int, expected):
    ret = did_not_get_two1(my_int)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("my_int, expected",
                         [
                             (2, False),
                             (1, True),
                             (3, True)
                         ])
def test_did_not_get_two2(my_int, expected):
    ret = did_not_get_two2(my_int)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("my_int1, my_int2, expected",
                         [
                             (1, 1, True),
                             (1, 2, False),
                             (2, 1, False),
                             (2, 2, True)
                         ])
def test_numbers_equal(my_int1, my_int2, expected):
    ret = numbers_equal(my_int1, my_int2)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("my_int, expected",
                         [
                             (1, False),
                             (2, False),
                             (3, True),
                             (4, True),
                             (5, False),
                             (6, False)
                         ])
def test_is_between_2_and_5(my_int, expected):
    ret = is_between_2_and_5(my_int)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("num, a, b, expected",
                         [
                             (1, 1, 2, False),
                             (0, 1, 2, False),
                             (2, 1, 2, False),
                             (9, 10, 13, False),
                             (10, 10, 13, False),
                             (11, 10, 13, True),
                             (12, 10, 13, True),
                             (13, 10, 13, False),
                             (14, 10, 13, False),
                         ])
def test_is_between_numbers(num, a, b, expected):
    ret = is_between_numbers(num, a, b)
    print("Answer returned: " + str(ret))
    assert ret == expected


@pytest.mark.parametrize("age, expected",
                         [
                             (-1, True),
                             (0, True),
                             (1, True),
                             (5, True),
                             (6, True),
                             (6.5, False),
                             (9, False),
                             (12, False),
                             (12.5, False),
                             (13, True),
                             (100, True),
                         ])
def test_not_in_elementary_school(age, expected):
    ret = not_in_elementary_school(age)
    print("Answer returned: " + str(ret))
    assert ret == expected


