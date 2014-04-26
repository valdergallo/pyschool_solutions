"""
Pairwise comparision of DNA sequences is a popular technique used in Bioinformatics.
It usually involves some scoring scheme to express the degree of similarity.
Write a function that compares two DNA sequences based on the following scoring
scheme: +1 for a match, +3 for each consecutive match and -1 for each mismatch.

Examples

>>> print pairwiseScore("ATTCGT", "ATCTAT")
ATTCGT
||   |
ATCTAT
Score: 2
>>> print pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")
GATAAATCTGGTCT
 ||  |||  |   
CATTCATCATGCAA
Score: 4
"""


def pairwiseScore(seqA, seqB):
    pairwiser = ""
    score = 0

    for i, letter in enumerate(seqA):
        if letter == seqB[i]:
            pairwiser += "|"
            score += 1
            if len(pairwiser) > 1 and pairwiser[i-1] == "|":
                score += 2
        else:
            pairwiser += " "
            score -= 1

    return "%s\n%s\n%s\nScore: %s" % (seqA, pairwiser, seqB, score)
