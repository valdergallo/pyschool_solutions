"""
Write a function hasSameContent(t1, t2) that takes in two tuples as arguments
and return True if both tuples contain the same items.

Examples

>>> hasSameContent((1, 2), (1, 2))
True

>>> hasSameContent((1, 2), (2, 1))
True

>>> hasSameContent((1, 2), (1, 2, 1))
False

>>> hasSameContent((1, 2), ())
False
"""


def hasSameContent(t1, t2):
    return sorted(t1) == sorted(t2)
