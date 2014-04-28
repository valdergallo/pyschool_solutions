"""
Sum Numbers
===========

In python, it is possible to pass in variable-length argument to a function by using the
following notation: *args. The argument is passed in as a tuple.

    def funA(*args):
        print type(args)
        print args

    >>> funA(1, 3, 5)
    <type 'tuple'>
    (1, 3, 5)

    >>> funA('a', 'b', 'c', 'd')
    <type 'tuple'>
    ('a', 'b', 'c', 'd')

Write a function sumNumbers(*args) that takes in a variable-length argument list of numbers
and returns the sum of the numbers.

Examples

>>> sumNumbers(1,2,3,4,5)
15
>>> sumNumbers(1,2,3)
6
>>> sumNumbers(1)
1
"""


def funA(*args):
    print type(args)
    print args


def sumNumbers(*args):
    return reduce(lambda x,y: x+y, args)
