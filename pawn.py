from piece import Piece

c = 0


class Pawn(Piece):
    def __init__(self, position = [0,0]):
        super().__init__(position)
        self.shape = ['♟', '♙']
        self.value = 1

    def move(self, dest):
        if (dest[0] <= 7 and dest[0] >= 0) and (self.position[1] == dest[1]) and (dest[1]-self.position[1] == 2) and c == 0:
            print('The move is valid')
            self.position = dest
            c = c+1
        if (dest[0] <= 7 and dest[0] >= 0) and (self.position[1] == dest[1]) and (dest[1]-self.position[1] == 1):
            print('The move is valid')
            self.position = dest
        else:
            print('The move is invalid')
            self.position = self.position
            return False
