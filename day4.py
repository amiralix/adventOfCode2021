from operator import contains
from posixpath import split
import numpy as np
import re

class board:
    marked = [] 
    self_board = [] 
    
    def __init__(self):
        self.marked = np.zeros((5,5))
        self.self_board = np.zeros((5,5))
    
    def mark(self,row,column):
        self.marked[row][column] = 1

    def is_win(self):
        is_win = False
        for row in range(0,5):
            if (  int(self.marked[row][0]) == 1 and 
                    (int(self.marked[row][0]) == int(self.marked[row][1])) and
                        (int(self.marked[row][1]) == int(self.marked[row][2])) and
                            ( int(self.marked[row][2]) == int(self.marked[row][3])) and 
                                (int(self.marked[row][3]) == int(self.marked[row][4]))  ):
                return row,0
        for column in range(0,5):
            if (  int(self.marked[0][column]) == 1 and 
                    (int(self.marked[0][column]) == int(self.marked[1][column])) and
                        (int(self.marked[1][column]) == int(self.marked[2][column])) and
                            ( int(self.marked[2][column]) == int(self.marked[3][column])) and 
                                (int(self.marked[3][column]) == int(self.marked[4][column]))  ):              
                return 0,column
        return -1,-1
    def set_self(self,input_matrix):
        for row in range(0,5):
            for column in range(0,5):
                self.self_board[row][column] = input_matrix[row][column]
    
    def find_number_in_board(self , number):
        for row in range(0,5):
            for column in range(0,5):
                if(self.self_board[row][column] == number):
                    return row,column     
        return -1
    def find_sum_unmarked(self):
        sum = 0
        for row in range(0,5):
            for column in range(0,5):
                if int(self.marked[row][column]) != 1 :
                    sum += self.self_board[row][column]
        return sum




with open("D:/new2.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]

boards = []
for counter in range(0,len(input)):
    input[counter] =  (re.split("\s",input[counter]))

for board_number in range(0,100):
    my_board = board()
    dirty_board = input[6*board_number+2:6*board_number+7]
    for row_counter in range(0,5):
        aRow = dirty_board[row_counter]
        clean_borad = []
        for column_counter in range(0,len(aRow)):
            if aRow[column_counter] != '' :
                clean_borad.append(aRow[column_counter])
        dirty_board[row_counter] = clean_borad
    my_board.set_self(dirty_board)
    boards.append(my_board)
    del my_board

win_boards_ever = [0] * 100

commands = input[0]
commands = commands[0].split(",")
for order_number in range(0,len(commands)):
    order = commands[order_number]
    for board_number in range(0, len(boards)):
        the_board = boards[board_number]
        if the_board.find_number_in_board(int(order)) != -1 :
            the_board.mark(the_board.find_number_in_board(int(order))[0],the_board.find_number_in_board(int(order))[1])
            if (the_board.is_win()[0] != -1 and  the_board.is_win()[1] != -1):
                win_boards_ever[board_number] = 1
                if win_boards_ever.count(0) == 0:
                    print(the_board.find_number_in_board(int(order))[0],the_board.find_number_in_board(int(order))[1])
                    print(board_number)
                    print(the_board.marked)
                    print("final item is" , order)
                    print("unmarked sum is" ,the_board.find_sum_unmarked())
                    print("answer is" , int(the_board.find_sum_unmarked())*int(order))
                    exit(0)

