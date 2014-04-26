"""
In the Risk board game, there is the situation where the attacker rolls 3 dice while the defender
rolls 2 dice. To determine the outcome, the highest die of each player is compared, followed by
the next highest die. For each case, the attacker's die has to be higher than that of the defender
to win. The loser will lose 1 army in each case.

Examples

>>> RiskGame([1,2,6], [1, 5])
'Defender loses 2 armies.'

>>> RiskGame([6,2,6], [6, 6])
'Attacker loses 2 armies.'

>>> RiskGame([1,4,1], [1, 2])
'Attacker loses 1 army and defender loses 1 army.'

"""


def RiskGame(attacker, defender):
    atk_loses = 0
    def_loses = 0

    attacker.sort(reverse=True)
    defender.sort(reverse=True)

    for i, j in zip(attacker, defender):
        if(i > j and i != j):
            def_loses += 1
        else:
            atk_loses += 1

    if atk_loses != 0 and def_loses != 0:
       return "Attacker loses %d army and defender loses %d army." % (atk_loses, def_loses)
    elif def_loses == 0 and atk_loses != 0:
       return "Attacker loses %d armies." % atk_loses
    elif atk_loses == 0 and def_loses != 0:
       return "Defender loses %d armies."  % def_loses
