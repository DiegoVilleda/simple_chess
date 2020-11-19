from piece import Piece


class Queen(Piece):
    def __init__(self, position = [0,0]):
        super().__init__(position)
        self.shape = ['♛','♕']
        self.value = 9

    def move(self, dest):
        if (dest[0] <= 7 and dest[0] >= 0) and ((dest[0] == self.position[0]) or (dest[1] == self.position[1]) or ((dest[0]-dest[1]) == (self.position[0]-self.position[1])) or (((dest[0]+dest[1]) == (self.position[0]+self.position[1])))):
            print('The move is valid')
            self.position = dest
        else:
            print('The move is invalid')
            self.position = self.position
            return False


if __name__ == "__main__":
    q = Queen([0,0])
    q.draw()

        
