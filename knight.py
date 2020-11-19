from piece import Piece

class Knight(Piece):
    def __init__(self, position = [0,0]):
        super().__init__(position)
        self.shape = ['♞','♘']
        self.value = 3

    def move(self, dest):
        if (dest [0] <= 7 and dest [0] >= 0) and((self.position[0]-dest[0])*(self.position[0]-dest[0])+(self.position[1]-dest[1])*(self.position[1]-dest[1])==5):
            print ('The move is valid')
            self.position = dest
        else:
            print('The move is invalid')
            self.position = self.position
            return False      
