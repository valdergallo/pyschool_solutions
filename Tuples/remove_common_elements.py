"""
Remove Common Elements
======================

Write a function removeCommonElements(t1, t2) that takes in 2 tuples as arguments and returns a sorted tuple containing elements that are not found in both tuples.

Examples

>>> removeCommonElements((1,2,3,4), (3,4,5,6))
(1, 2, 5, 6)
>>> removeCommonElements(('b','a','c','d'), ('a','b','c'))
('d',)
>>> removeCommonElements(('a','b','c'), ('a','b','c'))
()
>>> removeCommonElements(('a','b'), ('c', 'd'))
('a', 'b', 'c', 'd')
>>> removeCommonElements(('b','a','d','c'), ('a','b'))
('c', 'd')

"""

def removeCommonElements(t1, t2):
    uncommon = ()
    commons = tuple(set(t1) & set(t2))
    all_itens = sorted(t1 + t2)

    for i in all_itens:
        if i not in commons:
            uncommon += (i,)

    return uncommon
