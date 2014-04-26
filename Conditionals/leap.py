"""
Write a function that determines if a given year is a leap year.
A leap year is divisible by 4, but not by 100, unless it is also divisible by 400.

>>> LeapYear(2012)
True
>>> LeapYear(400)
True
>>> LeapYear(2010)
False
>>> LeapYear(100)
False

"""


def LeapYear(yr):
    leap = not bool(yr % 4) and bool(yr % 100) or not bool(yr % 400)
    return leap
