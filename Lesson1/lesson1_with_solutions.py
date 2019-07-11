import pytest


def return_str(my_str):
    """  תחזירו את המחרוזת שקיבלתם
    דוגמאות:
        "Aviad" ==> "Aviad"),
        "Ido"   ==> "Ido"
    """
    return my_str


def string_twice(my_str):
    """  תחזירו את המחרוזת שקיבלתם משורשרת פעמיים
    דוגמאות:
        "Aviad" ==> "AviadAviad"
        "Ido"   ==> "IdoIdo"
    """
    return my_str + my_str


def string_twice_with_space(my_str):
    """ החזירו את המחרוזת משורשרת פעמיים עם רווח באמצע
    דוגמאות:
        "Aviad" ==> "Aviad Aviad"
        "Ido"   ==> "Ido Ido"
    """
    return my_str + ' ' + my_str


def string_twice_with_newline(my_str):
    """ החזירו את המחרוזת משורשרת פעמיים עם שורה חדשה באמצע
    דוגמאות:
        "Aviad" ==> "Aviad
                     Aviad"
        "Ido"   ==> "Ido
                     Ido"
    """
    return my_str + "\n" + my_str


def my_name_is(name):
    """
    מקבלים שם
    תחזירו בדיוק את המשפט הבא כולל הגרשיים
    My name is "שם שקיבלתם"
    דוגמאות:
        "Ido"   ==> "My name is "Ido""
        "Aviad" ==> "My name is "Aviad""
     """
    return 'My name is "' + name + '"'


def mult(a, b):
    """ החזירו כפל מספרים שקיבלתם
    דוגמאות:
        a=3, b=4    ==> 12
        a=2, b=5    ==> 10
    """
    return a * b


def diff_in_age(big_brother_age_years, little_sister_age_months):
    """
        בהנתן גיל של האח הגדול (בשנים) וגיל של האחות התינוקת (בחודשים), החזירו את ההפרש בגילאים בחודשים
    דוגמאות:
        big_brother_age_years=12, little_sister_age_months=4    ==> 140
        big_brother_age_years=5, little_sister_age_months=4     ==> 56
    """
    return big_brother_age_years * 12 - little_sister_age_months


def months_sum_ages(age_years_brother1, age_years_brother2):
    """ בהנתן גילאים של שני אחים בשנים, החזר את מספר החודשים של סכום הגילאים שלהם.
    דוגמאות:
            age_years_brother1=12,  age_years_brother2=10   ==> 264
            age_years_brother1=4,   age_years_brother2= 8   ==> 144

    """
    return (age_years_brother1 + age_years_brother2) * 12


"""
====================================================================================
    הזהרה: טסטים מפה והלאה
====================================================================================
    WARNING: TESTs from here
====================================================================================    
"""


@pytest.mark.parametrize("input_str, expected",
                         [
                             ("Aviad", "Aviad"),
                             ("Ido", "Ido")
                         ])
def test_return_str(input_str, expected):
    ret = return_str(input_str)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("input_str, expected",
                         [
                             ("Aviad", "AviadAviad"),
                             ("Ido", "IdoIdo")
                         ])
def test_string_twice(input_str, expected):
    ret = string_twice(input_str)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("input_str, expected",
                         [
                             ("Aviad", "Aviad Aviad"),
                             ("Ido", "Ido Ido")
                         ])
def test_string_twice_with_space(input_str, expected):
    ret = string_twice_with_space(input_str)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("input_str, expected",
                         [
                             ("Aviad", "Aviad\nAviad"),
                             ("Ido", "Ido\nIdo")
                         ])
def test_string_twice_with_newline(input_str, expected):
    ret = string_twice_with_newline(input_str)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("input_str, expected",
                         [
                             ('Aviad', 'My name is "Aviad"'),
                             ('Ido', 'My name is "Ido"')
                         ])
def test_my_name_is(input_str, expected):
    ret = my_name_is(input_str)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("a, b, expected",
                         [
                             (3, 4, 12),
                             (2, 5, 10)
                         ])
def test_mult(a, b, expected):
    ret = mult(a, b)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("big_brother_age_years, little_sister_age_months, expected",
                         [
                             (12,   4,  140),
                             (5,    4,  56)
                         ])
def test_diff_in_age(big_brother_age_years, little_sister_age_months, expected):
    ret = diff_in_age(big_brother_age_years, little_sister_age_months)
    print(ret)
    assert ret == expected


@pytest.mark.parametrize("age_years_brother1, age_years_brother2, expected",
                         [
                             (12,   10, 264),
                             (4,    8,  144)
                         ])
def test_months_sum_ages(age_years_brother1, age_years_brother2, expected):
    ret = months_sum_ages(age_years_brother1, age_years_brother2)
    print(ret)
    assert ret == expected
