"""
In the pencil-and-paper game, Tic-tac-toe,
2 players take turns to mark 'X' and 'O' on a board of 3x3 squares.
The player who succeeds in marking 3 successive 'X' or 'O' in vertical,
horizontal or diagonal stripe wins the game. Write a function that determines
the outcome of a tic-tac-toe game.

Examples

>>> tictactoe([('X', ' ', 'O'),
...            (' ', 'O', 'O'),
...            ('X', 'X', 'X')])
"'X' wins (horizontal)."

# >>> tictactoe([('X', 'O', 'X'),
# ...            ('O', 'X', 'O'),
# ...            ('O', 'X', 'O') ])
# 'Draw.'

# >>> tictactoe([('X', 'O', 'O'),
# ...            ('X', 'O', ' '),
# ...            ('O', 'X', ' ') ])
# "'O' wins (diagonal)."

>>> tictactoe([('X', 'O', 'X'),
...            ('O', 'O', 'X'),
...            ('O', 'X', 'X') ])
"'X' wins (vertical)."
"""


def tictactoe(moves):
    winner = ''
    total_itens = []

    for i, line in enumerate(moves):
        if len(set(line)) == 1:
            winner = line[0]
            return "'%s' wins (horizontal)." % winner
        total_itens.extend(line)

    vertical = [total_itens[i::3] for i in xrange(3)]

    for line in vertical:
        if len(set(line)) == 1:
            winner = line[0]
            return "'%s' wins (vertical)." % winner

    diagonal = [total_itens[i:i-3] for i in xrange(3)]


    return 'Draw.'
