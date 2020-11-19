class Piece:
     def __init__(self, position = [0,0]):
         self.position = position
         self.color = ''
         self.shape = [' ',' ']
         self.value = 0

     def move (self, destination):
         pass
        
     def eat (self, destination):
         pass 



     def draw (self):
    
        print(' | ' + self.shape[self.color] +' ', end = '')

