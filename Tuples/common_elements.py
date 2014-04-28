"""
Common Elements
===============

Write a function commonElements(t1, t2) that takes in 2 tuples as arguments and returns
a sorted tuple containing elements that are found in both tuples.

Examples

>>> commonElements((1, 2, 3), (2, 5, 1))
(1, 2)
>>> commonElements((1, 2, 3, 'p', 'n'), (2, 5 ,1, 'p'))
(1, 2, 'p')
>>> commonElements((1, 3, 'p', 'n'), ('a', 2 , 5, 1, 'p'))
(1, 'p')
"""


def commonElements_with_set(t1, t2):
    return tuple(set(t1) & set(t2))


def commonElements_list_comprehensions(t1, t2):
    r = [i for i in t1 if i in t2]
    return tuple(r)


def commonElements(t1, t2):
    commons = ()
    for i in t1:
        if i in t2:
            commons += (i,)
    return commons
