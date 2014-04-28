"""
The determinant of a 2x2 matrix is the product of the elements on the main
diagonal minus the product of the elements off the main diagonal.

Examples

>>> M = ((3,1), (5,2))
>>> det(M)
1
"""

import numpy


def det_numpy(matrix):
    return numpy.linalg.det(matrix)


def det(matrix):
    "To calc matrix det: ab-bc"
    tl = len(matrix[0])  # total items in line
    diagonal = [matrix[i][i] for i in xrange(tl)]
    diagonal_revert = [matrix[i][(tl-1)-i] for i in xrange(tl)]

    mult_diagonal = reduce(lambda x, y: x*y, diagonal)
    mult_diagonal_revert = reduce(lambda x, y: x*y, diagonal_revert)

    return (mult_diagonal - mult_diagonal_revert)
