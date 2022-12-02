from random import *

class TicTacToe:
    def __init__(self):
        self.board = [False for i in range(9)]
    
    def show(self):
        a = [' ', 'x', 'o']
        print(a[self.board[0]], '|', a[self.board[1]], '|', a[self.board[2]])
        print('---------')
        print(a[self.board[3]], '|', a[self.board[4]], '|', a[self.board[5]])
        print('---------')
        print(a[self.board[6]], '|', a[self.board[7]], '|', a[self.board[8]])

    def win(self, player):
        b = self.board
        if b[0] == player:
            if b[0] == b[1] and b[1] == b[2]:
                return True
            if b[0] == b[4] and b[4] == b[8]:
                return True
            if b[0] == b[3] and b[3] == b[6]:
                return True
        if b[1] == player:
            if b[1] == b[4] and b[4] == b[7]:
                return True
        if b[2] == player:
            if b[2] == b[5] and b[5] == b[8]:
                return True
            if b[2] == b[4] and b[4] == b[6]:
                return True
        if b[3] == player:
            if b[3] == b[4] and b[4] == b[5]:
                return True
        if b[6] == player:
            if b[6] == b[7] and b[7] == b[8]:
                return True
        return False
    
    def is_filled(self):
        return False not in self.board
    
    def is_over(self):
        return self.win(1) or self.win(-1) or self.is_filled()
    
    def get_move(self, player):
        self.show()
        n = int(input('what square: '))
        while self.board[n]:
            n = int(input('square taken!\nwhat square: '))
        self.board[n] = player

    def game(self):
        while not self.is_over():
            self.get_move(1)
            if self.is_over():
                break
            self.get_move(-1)
        self.show()
        if self.win(1):
            print('x wins!')
        elif self.win(-1):
            print('o wins!')
        else:
            print('draw')
