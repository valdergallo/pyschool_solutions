"""
For a quadratic equation in the form of ax2 + bx + c, the discriminant, D is b2-4ac.
Write a function that return the following output depending on the discriminant.
D > 0: 2 real roots.
D = 0: 1 real root.
D < 0: 2 complex roots.


>>> quadratic(1, 2, 3)
'This equation has 2 complex roots.'
>>> quadratic(1, 3, 2)
'This equation has 2 real roots.'
>>> quadratic(1, 4, 4)
'This equation has 1 real root.'

"""


def quadratic(a, b, c):
    D = (b ** 2) - (4 * a * c)

    if D > 0:
        return 'This equation has 2 real roots.'
    elif D == 0:
        return 'This equation has 1 real root.'
    elif D < 0:
        return 'This equation has 2 complex roots.'
