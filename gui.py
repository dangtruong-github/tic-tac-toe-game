from commons import *
from board import Board
from tkinter import *

class GUIBoard:
    def __init__(self, size, board = -1):
        self.board = Board(size, board)

        self.turn = X_TURN['value']

        self.window = Tk()

        self.tk_board = []
        for i in range(size[0]):
            self.tk_board.append([])
            for j in range(size[1]):
                def create_lambda(pos=[i,j]):
                    return lambda pos=pos: self.move(pos)
                new_button = Button(self.window, text=BLANK['text'], font=("Arial", 20), state='normal', bg='white', command=create_lambda())
                self.tk_board[i].append(new_button)
        
        for i in range(size[0]):
            for j in range(size[1]):
                self.tk_board[i][j].grid(row=i, column=j)

        # Start the GUI
        self.window.mainloop()

    
    def update(self):
        for i in range(self.board.size[0]):
            for j in range(self.board.size[1]):
                state = 'normal' if self.board.board[i][j] == BLANK["text"] else 'disabled'
                self.tk_board[i][j].config(state=state, text=self.board.board[i][j])
    
    def move(self, pos):
        move_status = self.board.move(pos, self.turn)
        if move_status:
            self.turn *= -1
            self.update()
        return move_status