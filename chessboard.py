from queen import Queen
from pawn import Pawn
from bishop import Bishop
from king import King
from knight import Knight
from rook import Rook


class Chessboard():
    def __init__(self):
        self.squares = [[Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()],
                        [Pawn(), Pawn(), Pawn(), Pawn(),
                         Pawn(), Pawn(), Pawn(), Pawn()],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [Pawn(), Pawn(), Pawn(), Pawn(),
                         Pawn(), Pawn(), Pawn(), Pawn()],
                        [Rook(), Knight(), Bishop(), Queen(),
                         King(), Bishop(), Knight(), Rook()],
                        ]
        for row in range(len(self.squares)):
            for col in range(len(self.squares[0])):
                p = self.squares[row][col]
                if p:
                    p.position = [row, col]
                    p.color = (1 if row < 4 else 0)

    def draw(self):
        for row in range(len(self.squares)):
            for col in range(len(self.squares[0])):
                p = self.squares[row][col]
                if p:
                    p.draw()
                else:
                    print(' |   ', end='')
            print(' | ')
            print(' |', end='')
            for col in range(len(self.squares[0])):
                print('____|', end='')
            print(f'{row}')
        print('   0    1    2    3    4     5    6   7   ')
    def move(self, origin, destination):
        print(f'from: {origin} to: {destination}')
        return True


if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.draw()
