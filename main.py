from chessboard import Chessboard


if __name__ == "__main__":
    chessboard = Chessboard()
    chessboard.draw()
    print('white player turn')
    o = input('Please introduce the origin square:')
    d = input('Please introduce the destination square:')
    chessboard.move(o,d)

    print('black  player turn')
    o = input('Please introduce the origin square:')
    d = input('Please introduce the destination square:')
    chessboard.move(o,d)