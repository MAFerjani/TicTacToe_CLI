"""
Extremely simple implementation of Tic Tac Toe for two players, named Jaber and Salah.
This implementation treats the board as a 1D array with 9 values, each value represnet a cell in the board, numbering strating from the top left to the bottom right
"""

class Board:
    def __init__(self):
        self.s = list(range(1,10))

    def __str__(self):
        return f"\n{self.s[0]}|{self.s[1]}|{self.s[2]}\n{self.s[3]}|{self.s[4]}|{self.s[5]}\n{self.s[6]}|{self.s[7]}|{self.s[8]}\n"

    def check(self):
        WIN_PATTERNS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

        for i in WIN_PATTERNS:
            if self.s[i[0]] == self.s[i[1]] == self.s[i[2]]:
                return True
        return False

board = Board()
print(board)

# our players in list of lists
players = [['Jaber','X'], ['Salah','O']]

pl_i = 1 # player index
played_squares = [] # to keep a track of the places that were played
tie = False # to end when the game ends in a tie

# Game loop
while not board.check():
    pl_i = abs(pl_i-1) # to alternate between players

    # This breaks out when the game ends in a tie
    if played_squares == list(range(1, 10)):
        tie = True
        break

    place = input(f'Where do you want to put {players[pl_i][1]} Mr.{players[pl_i][0]}\n')

    # if the user inputs a non-valid square number
    if place not in str(list(range(1,10))):
        print('Not a valid square number, try again!')
        pl_i = abs(pl_i - 1)
        continue
    else:
        place = int(place)

    # the following makes sure that the chosen place was not used yet
    if place in played_squares:
        print(f"don't cheat Mr.{players[pl_i][0]}\n")
        pl_i = abs(abs(pl_i - 1))
        continue

    played_squares.append(place)
    played_squares.sort()
    place -= 1  # because the index of the squares is not as printed to the user

    board.s[place] = players[pl_i][1]
    print(board)


if not tie:
    print(f'{players[pl_i][0]} is the winner')
else:
    print('tied game gg for both :)')
