from piece import Piece

class King(Piece):
    def __init__(self, position = [0,0]):
        super().__init__(position)
        self.shape = ['♚','♔']
        self.value = 10

    def move(self, dest):
        if (dest [0] <= 7 and dest [0] >= 0) and((abs(self.position[0]-dest[0])<=1 and (abs(self.position[1]-dest[1])<=1))) :
            print ('The move is valid')
            self.position = dest
        else:
            print('The move is invalid')
            self.position = self.position
            return False
