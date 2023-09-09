from commons import *

class Board:
    def __init__(self, size, board = -1):
        self.size = size
        self.board = board
        
        if board == -1:
            self.board = []
            for i in range(size[0]):
                self.board.append([])
                for j in range(size[1]):
                    self.board[i].append(BLANK["text"])

    def move(self, pos, turn):
        if self.board[pos[0]][pos[1]] != BLANK["text"]:
            return False
        print(pos, turn)
        self.board[pos[0]][pos[1]] = X_TURN["text"] if turn > 0 else O_TURN["text"]
        return True